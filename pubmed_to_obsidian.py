import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
import re
import time
import subprocess
from Bio import Entrez
from datetime import datetime
from pyzotero import zotero

# --- 配置区 ---
EMAIL = "duanwenqiang1227@gmail.com" 
SEARCH_QUERY = '("Breast Neoplasms"[Mesh]) AND ("HR positive" OR "HR+") AND ("HER2 negative" OR "HER2-")'
ZOTERO_COLLECTION_NAME = "医学信息订阅"

# 从环境变量读取 Zotero 凭证
ZOTERO_USER_ID = os.environ.get('ZOTERO_USER_ID')
ZOTERO_API_KEY = os.environ.get('ZOTERO_API_KEY')

# 期刊及其最新 IF 映射 (2025 JCR 数据)
JOURNAL_IF_MAP = {
    # 顶级医学综合
    "The New England Journal of Medicine": "158.5",
    "The Lancet": "145.0",
    "JAMA": "120.7",
    "BMJ": "93.6",
    # 顶级肿瘤评论与统计
    "CA: A Cancer Journal for Clinicians": "232.4",
    "Nature Reviews Clinical Oncology": "82.2",
    # 临床巨头
    "Annals of Oncology": "56.7",
    "Journal of Clinical Oncology": "42.1",
    "The Lancet Oncology": "41.6",
    "JAMA Oncology": "22.5",
    "Journal of hematology & oncology": "25.2",
    # 转化与基础研究
    "Cancer Cell": "48.8",
    "Signal Transduction and Targeted Therapy": "40.8",
    "Cancer Discovery": "29.7",
    "Nature Cancer": "28.5",
    "Molecular Cancer": "27.7",
    "Cancer Communications": "20.1",
    "Trends in Cancer": "14.3",
    "Cancer Research": "12.5",
    "Cell Reports Medicine": "11.7",
    "Med": "12.8",
    "JNCI: Journal of the National Cancer Institute": "10.3",
    "Clinical Cancer Research": "10.0",
    # 领域权威 (保留部分 5-10 分的高质量专业杂志)
    "The Breast": "7.9",
    "npj Breast Cancer": "6.5",
    "Breast Cancer Research": "5.6",
    "Breast Cancer Research and Treatment": "4.9"
}

def gemini_deep_analyze(title, abstract):
    """调用 Gemini CLI 进行乳腺癌临床深度分析"""
    print(f"正在调用 Gemini 解析文献: {title[:50]}...")
    prompt = f"""
    你是一位乳腺癌转化医学与临床专家。请深入分析以下文献摘要，并为一名临床医生提供专业总结。
    
    文献标题：{title}
    摘要内容：{abstract}
    
    请输出以下结构化内容（使用中文）：
    ## 🧬 Gemini 临床深度解析
    - **分型与人群:** (明确是 HR+/HER2-, TNBC 还是 HER2+；早期还是晚期)
    - **PICO 核心:** 
        - **P (Patient):** 患者特征
        - **I (Intervention):** 干预措施
        - **C (Comparison):** 对照方案
        - **O (Outcome):** 核心终点指标
    - **临床价值:** (该研究是否挑战现有指南？对临床决策有何直接影响？)
    - **关键数据:** (提取 HR, ORR, pCR 或 OS/PFS 等关键数值)
    - **专家评述:** (该研究是否存在偏倚？后续关注点是什么？)
    """
    
    # 定义可能的命令名
    commands_to_try = ['gemini', 'gemini-cli', '/usr/local/bin/gemini']
    
    last_error = ""
    for cmd in commands_to_try:
        try:
            # 使用 shell=True 确保能从系统 PATH 中搜寻到 npm 安装的命令
            result = subprocess.run(f"{cmd} '{prompt}'", shell=True, capture_output=True, text=True, encoding='utf-8')
            if result.returncode == 0:
                return result.stdout.strip()
            last_error = result.stderr
        except Exception as e:
            last_error = str(e)
            continue
            
    return f"\n> [!warning] Gemini 解析失败\n> {last_error if last_error else '找不到可用的 gemini 命令。'}"

def get_or_create_collection(zot, name):
    collections = zot.collections()
    for col in collections:
        if col['data']['name'] == name:
            return col['key']
    
    resp = zot.create_collections([{'name': name}])
    if resp['successful']:
        return resp['successful']['0']['key']
    return None

def fetch_papers():
    Entrez.email = EMAIL
    journal_terms = " OR ".join([f'"{j}"[Journal]' for j in JOURNAL_IF_MAP.keys()])
    full_query = f"({SEARCH_QUERY}) AND ({journal_terms})"
    handle = Entrez.esearch(db="pubmed", term=full_query, reldate=30, datetype="pdat")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    if not id_list: return []
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="xml")
    papers = Entrez.read(handle)
    return papers['PubmedArticle']

def parse_date(pub_date_data):
    year = pub_date_data.get('Year', 'Unknown')
    month_map = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    month = pub_date_data.get('Month', '01')
    if month in month_map: month = month_map[month]
    day = pub_date_data.get('Day', '01')
    if year == 'Unknown': return "Unknown"
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

def clean_filename(title):
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    return title[:120]

def sync_to_zotero(title, journal, doi, pmid):
    if not ZOTERO_USER_ID or not ZOTERO_API_KEY:
        return None
    zot = zotero.Zotero(ZOTERO_USER_ID, 'user', ZOTERO_API_KEY)
    col_key = get_or_create_collection(zot, ZOTERO_COLLECTION_NAME)
    
    search_results = zot.everything(zot.items(q=doi))
    if search_results:
        item = search_results[0]
        if col_key and col_key not in item['data'].get('collections', []):
            item['data']['collections'].append(col_key)
            zot.update_item(item)
        return item['key']
    
    template = zot.item_template('journalArticle')
    template['title'] = title
    template['publicationTitle'] = journal
    template['DOI'] = doi
    template['extra'] = f"PMID: {pmid}"
    if col_key:
        template['collections'] = [col_key]
    
    resp = zot.create_items([template])
    if resp['successful']:
        item_key = resp['successful']['0']['key']
        return item_key
    return None

def format_to_md(article):
    medline = article['MedlineCitation']
    article_data = medline['Article']
    title = article_data['ArticleTitle']
    journal = article_data.get('Journal', {}).get('Title', 'Unknown')
    
    if_value = "N/A"
    for j_name, if_val in JOURNAL_IF_MAP.items():
        if j_name.lower() in journal.lower():
            if_value = if_val
            break

    pub_date_str = parse_date(article_data['Journal']['JournalIssue']['PubDate'])
    year = pub_date_str.split('-')[0]
    
    doi = ""
    for x in article['PubmedData']['ArticleIdList']:
        if x.attributes.get('IdType') == 'doi': doi = str(x)
    
    abstract_text = ""
    if 'Abstract' in article_data:
        abstract_text = "\n".join(article_data['Abstract']['AbstractText'])
    
    # 同步到 Zotero 
    zotero_key = sync_to_zotero(title, journal, doi, medline['PMID'])
    zotero_link = f"zotero://select/items/0_{zotero_key}" if zotero_key else "Not Synced"

    # 调用 Gemini 进行深度解析
    gemini_analysis = gemini_deep_analyze(title, abstract_text)

    # 文件名优化：[年份] 标题
    safe_title = clean_filename(title)
    filename = f"Papers/[{year}] {safe_title}.md"
    
    content = f"""---
title: "{title}"
journal: "{journal}"
if: {if_value}
published: "{pub_date_str}"
doi: "{doi}"
pmid: {medline['PMID']}
zotero_link: "{zotero_link}"
tags: #BC #HR+HER2- #HighIF #GeminiAnalyzed
sync_date: {datetime.now().strftime('%Y-%m-%d')}
---
# {title}

- **Journal**: {journal} (**IF: {if_value}**)
- **Published**: {pub_date_str} | **PMID**: {medline['PMID']}
- **DOI**: [{doi}](https://doi.org/{doi})
- **Zotero**: [点击跳转 Zotero 库]({zotero_link})

{gemini_analysis}

## 📄 Abstract
{abstract_text}
"""
    return filename, content, {
        "pmid": medline['PMID'], 
        "title": f"[{year}] {safe_title}", 
        "full_title": title,
        "journal": journal, 
        "if": if_value,
        "pub_date": pub_date_str,
        "zotero_link": zotero_link
    }

def update_index(all_papers):
    index_file = "BC_Papers_Index.md"
    header = "# BC Papers Index\n\n| No. | IF | Published | Journal | Title | Zotero | Link |\n| --- | --- | --- | --- | --- | --- | --- |\n"
    all_papers.sort(key=lambda x: float(x['if']) if x['if'] != 'N/A' else 0, reverse=True)
    
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(header)
        for idx, info in enumerate(all_papers, 1):
            z_link = f"[Link]({info['zotero_link']})" if "zotero://" in info['zotero_link'] else "-"
            line = f"| {idx} | {info['if']} | {info['pub_date']} | {info['journal']} | {info['full_title']} | {z_link} | [[{info['title']}]] |\n"
            f.write(line)

if __name__ == "__main__":
    if not os.path.exists("/Users/kurt-d/Documents/Tuan仓元/Papers"): os.makedirs("/Users/kurt-d/Documents/Tuan仓元/Papers")
    
    # 检查环境变量
    if not ZOTERO_USER_ID or not ZOTERO_API_KEY:
        print("警告: 环境变量 ZOTERO_USER_ID 或 ZOTERO_API_KEY 未设置。文献将不会同步到 Zotero。")
    
    print("正在从 PubMed 抓取乳腺癌 HR+/HER2- 最新文献...")
    papers = fetch_papers()
    print(f"找到 {len(papers)} 篇文献。")
    
    all_current_info = []
    for p in papers:
        result = format_to_md(p)
        if result:
            fname, text, info = result
            # 写入 Obsidian
            with open(fname, "w", encoding="utf-8") as f:
                f.write(text)
            all_current_info.append(info)
            print(f"已完成: {info['title'][:60]}...")
    
    if all_current_info:
        update_index(all_current_info)
        print(f"\n✅ 任务完成！")
        print(f"- 笔记位置: Papers/ 文件夹")
        print(f"- 索引更新: BC_Papers_Index.md")
        print(f"- 精读解析: Gemini 已自动完成 PICO 总结。")
