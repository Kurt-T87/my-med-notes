import os
import re
from Bio import Entrez
from datetime import datetime

# --- 配置区 ---
EMAIL = "duanwenqiang1227@gmail.com" 
SEARCH_QUERY = '("Breast Neoplasms"[Mesh]) AND ("HR positive" OR "HR+") AND ("HER2 negative" OR "HER2-")'

# 期刊及其 IF 映射
JOURNAL_IF_MAP = {
    "CA: A Cancer Journal for Clinicians": "232.4",
    "Nature Reviews Clinical Oncology": "82.2",
    "Annals of Oncology": "65.4",
    "Journal of Clinical Oncology": "41.9",
    "Lancet Oncology": "35.9",
    "Cancer Cell": "44.5",
    "Signal Transduction and Targeted Therapy": "40.8",
    "Molecular Cancer": "33.9",
    "Cancer Discovery": "33.3",
    "Cancer Communications": "24.9",
    "JAMA Oncology": "20.1",
    "Clinical Cancer Research": "10.2",
    "The Breast": "7.9",
    "npj Breast Cancer": "7.6",
    "Breast Cancer Research": "5.6",
    "Breast Cancer Research and Treatment": "4.9",
    "Annals of oncology : official journal of the European Society for Medical Oncology": "65.4",
    "Journal of clinical oncology : official journal of the American Society of Clinical Oncology": "41.9",
    "The Lancet. Oncology": "35.9",
    "Breast cancer research : BCR": "5.6",
    "Breast cancer research and treatment": "4.9"
}

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
    month_map = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }
    month = pub_date_data.get('Month', '01')
    if month in month_map: month = month_map[month]
    day = pub_date_data.get('Day', '01')
    if not re.match(r'^\d+$', str(month)): month = '01'
    if not re.match(r'^\d+$', str(day)): day = '01'
    if year == 'Unknown': return "Unknown"
    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

def clean_filename(title):
    # 移除非法字符，保留空格，缩短长度
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    return title[:120] # 防止文件名过长

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
    doi = ""
    for x in article['PubmedData']['ArticleIdList']:
        if x.attributes.get('IdType') == 'doi': doi = str(x)
    abstract_text = ""
    if 'Abstract' in article_data:
        abstract_text = "\n".join(article_data['Abstract']['AbstractText'])
    
    # 使用标题命名
    safe_title = clean_filename(title)
    filename = f"Papers/{safe_title}.md"
    
    content = f"""---
title: "{title}"
journal: "{journal}"
if: {if_value}
published: "{pub_date_str}"
doi: "{doi}"
pmid: {medline['PMID']}
tags: #BC #HR+HER2- #HighIF
sync_date: {datetime.now().strftime('%Y-%m-%d')}
---
# {title}

- **Journal**: {journal} (**IF: {if_value}**)
- **Published**: {pub_date_str}
- **PMID**: {medline['PMID']}
- **DOI**: [{doi}](https://doi.org/{doi})

## Abstract
{abstract_text}
"""
    return filename, content, {
        "pmid": medline['PMID'], 
        "title": safe_title, # 使用安全标题
        "full_title": title,
        "journal": journal, 
        "if": if_value,
        "pub_date": pub_date_str
    }

def update_index(all_papers):
    index_file = "BC_Papers_Index.md"
    # 表头新增 No. 序列号列
    header = "# BC Papers Index\n\n| No. | IF | Published | Journal | Title | Link |\n| --- | --- | --- | --- | --- | --- |\n"
    
    # 按 IF 排序
    all_papers.sort(key=lambda x: float(x['if']) if x['if'] != 'N/A' else 0, reverse=True)
    
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(header)
        for idx, info in enumerate(all_papers, 1):
            line = f"| {idx} | {info['if']} | {info['pub_date']} | {info['journal']} | {info['full_title']} | [[{info['title']}]] |\n"
            f.write(line)

if __name__ == "__main__":
    if not os.path.exists("Papers"): os.makedirs("Papers")
    papers = fetch_papers()
    print(f"Found {len(papers)} papers.")
    
    all_current_info = []
    for p in papers:
        result = format_to_md(p)
        if result:
            fname, text, info = result
            with open(fname, "w", encoding="utf-8") as f:
                f.write(text)
            all_current_info.append(info)
    
    if all_current_info:
        update_index(all_current_info)
        print(f"Index updated with {len(all_current_info)} papers.")
