import os
from Bio import Entrez
from datetime import datetime

# --- 配置区 ---
EMAIL = "your-email@example.com"  # 请在使用时手动改一下这里的邮箱！
SEARCH_QUERY = '("Breast Neoplasms"[Mesh]) AND ("HR positive" OR "HR+") AND ("HER2 negative" OR "HER2-")'
# 高分/顶级期刊名单 (根据 ScholarScope 的标准)
TOP_JOURNALS = [
    "The New England journal of medicine", "The Lancet", "Journal of clinical oncology", 
    "Nature medicine", "Annals of oncology", "JAMA oncology", "Lancet oncology",
    "Nature", "Science", "Cell", "Cancer cell", "Journal of the National Cancer Institute"
]

def fetch_papers():
    Entrez.email = EMAIL
    # 搜索过去 30 天内发表的文章
    handle = Entrez.esearch(db="pubmed", term=SEARCH_QUERY, reldate=30, datetype="pdat")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    if not id_list: return []
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="xml")
    papers = Entrez.read(handle)
    return papers['PubmedArticle']

def format_to_md(article):
    medline = article['MedlineCitation']
    article_data = medline['Article']
    title = article_data['ArticleTitle']
    journal = article_data.get('Journal', {}).get('Title', 'Unknown')
    if journal.lower() not in [j.lower() for j in TOP_JOURNALS]:
        return None
    doi = ""
    for x in article['PubmedData']['ArticleIdList']:
        if x.attributes.get('IdType') == 'doi': doi = str(x)
    abstract_text = ""
    if 'Abstract' in article_data:
        abstract_text = "\n".join(article_data['Abstract']['AbstractText'])
    
    # 笔记文件名
    filename = f"Papers/{medline['PMID']}.md"
    content = f"""---
title: "{title}"
journal: "{journal}"
doi: "{doi}"
tags: #BC #HR+HER2- #HighIF
date: {datetime.now().strftime('%Y-%m-%d')}
---
# {title}
**Journal**: {journal} | **DOI**: [{doi}](https://doi.org/{doi})
## Abstract
{abstract_text}
"""
    return filename, content

if __name__ == "__main__":
    if not os.path.exists("Papers"): os.makedirs("Papers")
    papers = fetch_papers()
    for p in papers:
        result = format_to_md(p)
        if result:
            fname, text = result
            with open(fname, "w", encoding="utf-8") as f:
                f.write(text)
