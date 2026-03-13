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
# 扩展检索词，包含 ER/PR 等不同写法
SEARCH_QUERY = '("Breast Neoplasms"[Mesh]) AND ("HR positive" OR "HR+" OR "ER positive" OR "ER+") AND ("HER2 negative" OR "HER2-")'
ZOTERO_COLLECTION_NAME = "医学信息订阅"

# 从环境变量读取 Zotero 凭证
ZOTERO_USER_ID = os.environ.get('ZOTERO_USER_ID')
ZOTERO_API_KEY = os.environ.get('ZOTERO_API_KEY')

# 期刊及其最新 IF 映射 (2025 JCR 数据)
# 包含大量缩写，确保匹配成功率
JOURNAL_IF_MAP = {
    "The New England Journal of Medicine": "158.5", "N Engl J Med": "158.5",
    "The Lancet": "145.0", "Lancet": "145.0",
    "JAMA": "120.7",
    "BMJ": "93.6",
    "CA: A Cancer Journal for Clinicians": "232.4", "CA Cancer J Clin": "232.4",
    "Nature Reviews Clinical Oncology": "82.2", "Nat Rev Clin Oncol": "82.2",
    "Annals of Oncology": "56.7", "Ann Oncol": "56.7",
    "Journal of Clinical Oncology": "42.1", "J Clin Oncol": "42.1",
    "The Lancet Oncology": "41.6", "Lancet Oncol": "41.6",
    "JAMA Oncology": "22.5", "JAMA Oncol": "22.5",
    "Journal of hematology & oncology": "25.2", "J Hematol Oncol": "25.2",
    "Cancer Cell": "48.8",
    "Signal Transduction and Targeted Therapy": "40.8", "Signal Transduct Target Ther": "40.8",
    "Cancer Discovery": "29.7", "Cancer Discov": "29.7",
    "Nature Cancer": "28.5", "Nat Cancer": "28.5",
    "Molecular Cancer": "27.7", "Mol Cancer": "27.7",
    "Cancer Communications": "20.1", "Cancer Commun": "20.1",
    "Nature Communications": "14.7", "Nat Commun": "14.7",
    "Trends in Cancer": "14.3",
    "Cancer Research": "12.5", "Cancer Res": "12.5",
    "Cell Reports Medicine": "11.7", "Cell Rep Med": "11.7",
    "Med": "12.8",
    "JNCI: Journal of the National Cancer Institute": "10.3", "J Natl Cancer Inst": "10.3",
    "Clinical Cancer Research": "10.0", "Clin Cancer Res": "10.0",
    "The Breast": "7.9", "Breast": "7.9",
    "npj Breast Cancer": "6.5",
    "Breast Cancer Research": "5.6", "Breast Cancer Res": "5.6",
    "Breast Cancer Research and Treatment": "4.9", "Breast Cancer Res Treat": "4.9",
    "European Journal of Cancer": "7.6", "Eur J Cancer": "7.6",
    "British Journal of Cancer": "7.6", "Br J Cancer": "7.6",
    "Oncogene": "8.0",
    "Theranostics": "11.6",
    "Science Translational Medicine": "15.8", "Sci Transl Med": "15.8"
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
    
    commands_to_try = ['gemini', 'gemini-cli', '/usr/local/bin/gemini']
    
    last_error = ""
    for cmd in commands_to_try:
        try:
            result = subprocess.run([cmd, "-p", prompt], capture_output=True, text=True, encoding='utf-8')
            if result.returncode == 0:
                return result.stdout.strip()
            
            stderr_output = result.stderr.lower()
            if "quota" in stderr_output or "limit" in stderr_output:
                return "\n> [!info] Gemini 临床精读解析暂不可用（API 每日免费额度已耗尽）。已为你保留原始摘要供查阅。"
            
            last_error = f"Code: {result.returncode}, Error: {result.stderr}"
        except Exception:
            continue
            
    return f"\n> [!warning] Gemini 解析失败\n> {last_error if last_error else '服务暂时不可用'}"

def get_or_create_collection(zot, name):
    collections = zot.collections()
    for col in collections:
        if col['data']['name'] == name:
            return col['key']
    resp = zot.create_collections([{'name': name}])
    return resp['successful']['0']['key'] if resp['successful'] else None

def fetch_papers():
    Entrez.email = EMAIL
    # 重要修改：不再在 PubMed 端锁定期刊，而是在脚本内过滤，防止遗漏
    handle = Entrez.esearch(db="pubmed", term=SEARCH_QUERY, reldate=30, datetype="pdat", retmax=50)
    record = Entrez.read(handle)
    id_list = record["IdList"]
    if not id_list: return []
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="xml")
    papers = Entrez.read(handle)
    return papers['PubmedArticle']

def parse_date(pub_date_data):
    year = pub_date_data.get('Year', 'Unknown')
    month = pub_date_data.get('Month', '01')
    month_map = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    if month in month_map: month = month_map[month]
    day = pub_date_data.get('Day', '01')
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

def clean_filename(title):
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    return title[:120]

def sync_to_zotero(title, journal, doi, pmid):
    if not ZOTERO_USER_ID or not ZOTERO_API_KEY: return None
    zot = zotero.Zotero(ZOTERO_USER_ID, 'user', ZOTERO_API_KEY)
    col_key = get_or_create_collection(zot, ZOTERO_COLLECTION_NAME)
    search_results = zot.everything(zot.items(q=doi))
    if search_results: return search_results[0]['key']
    template = zot.item_template('journalArticle')
    template.update({'title': title, 'publicationTitle': journal, 'DOI': doi, 'extra': f"PMID: {pmid}"})
    if col_key: template['collections'] = [col_key]
    resp = zot.create_items([template])
    return resp['successful']['0']['key'] if resp['successful'] else None

def format_to_md(article):
    medline = article['MedlineCitation']
    article_data = medline['Article']
    title = article_data['ArticleTitle']
    journal = article_data.get('Journal', {}).get('Title', 'Unknown')
    
    if_value = "N/A"
    # 模糊匹配期刊名
    for j_name, if_val in JOURNAL_IF_MAP.items():
        if j_name.lower() in journal.lower() or journal.lower() in j_name.lower():
            if_value = if_val
            break

    pub_date_str = parse_date(article_data['Journal']['JournalIssue']['PubDate'])
    year = pub_date_str.split('-')[0]
    doi = next((str(x) for x in article['PubmedData']['ArticleIdList'] if x.attributes.get('IdType') == 'doi'), "")
    abstract_text = "\n".join(article_data['Abstract']['AbstractText']) if 'Abstract' in article_data else "No Abstract"
    
    zotero_key = sync_to_zotero(title, journal, doi, medline['PMID'])
    zotero_link = f"zotero://select/items/0_{zotero_key}" if zotero_key else "Not Synced"
    gemini_analysis = gemini_deep_analyze(title, abstract_text)

    # 只要是相关文献，即使 IF 未知也先保留，避免遗漏
    final_if = if_value if if_value != "N/A" else "Unknown"
    
    filename = f"Papers/[{year}] {clean_filename(title)}.md"
    content = f"""---
title: "{title}"
journal: "{journal}"
if: {final_if}
published: "{pub_date_str}"
doi: "{doi}"
pmid: {medline['PMID']}
zotero_link: "{zotero_link}"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: {datetime.now().strftime('%Y-%m-%d')}
---
# {title}
- **Journal**: {journal} (**IF: {final_if}**)
- **Published**: {pub_date_str} | **PMID**: {medline['PMID']}
- **DOI**: [{doi}](https://doi.org/{doi})
- **Zotero**: [点击跳转 Zotero 库]({zotero_link})

{gemini_analysis}

## 📄 Abstract
{abstract_text}
"""
    return filename, content, {"pmid": medline['PMID'], "title": f"[{year}] {clean_filename(title)}", "full_title": title, "journal": journal, "if": final_if, "pub_date": pub_date_str, "zotero_link": zotero_link}

def update_index(all_papers):
    index_file = "BC_Papers_Index.md"
    header = "# BC Papers Index\n\n| No. | IF | Published | Journal | Title | Zotero | Link |\n| --- | --- | --- | --- | --- | --- | --- |\n"
    all_papers.sort(key=lambda x: float(x['if']) if x['if'] not in ['N/A', 'Unknown'] else 0, reverse=True)
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(header)
        for idx, info in enumerate(all_papers, 1):
            f.write(f"| {idx} | {info['if']} | {info['pub_date']} | {info['journal']} | {info['full_title']} | [Link]({info['zotero_link']}) | [[{info['title']}]] |\n")

if __name__ == "__main__":
    if not os.path.exists("Papers"): os.makedirs("Papers")
    print("正在以 [大网模式] 抓取乳腺癌 HR+/HER2- 最新文献...")
    papers = fetch_papers()
    print(f"找到 {len(papers)} 篇潜在相关文献。")
    all_current_info = []
    for p in papers:
        res = format_to_md(p)
        if res:
            fname, text, info = res
            with open(fname, "w", encoding="utf-8") as f: f.write(text)
            all_current_info.append(info)
            print(f"已处理: {info['full_title'][:50]}...")
    if all_current_info: update_index(all_current_info)
    print("\n✅ 任务完成！请在 Obsidian 中查看 Papers/ 文件夹。")
