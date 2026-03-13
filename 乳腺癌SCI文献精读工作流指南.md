---
title: 乳腺癌 SCI 文献精读工作流指南
tags:
  - workflow
  - medicine
  - breast-cancer
  - gemini
  - guide
created: 2026-03-13
---

# 📑 乳腺癌 SCI 文献精读工作流指南 

本工作流实现了从 **PubMed 抓取** -> **Gemini 专家解析** -> **Zotero 同步** -> **Obsidian 知识内化** 的全自动化闭环。

---

## 🛠️ 核心架构
- **自动化引擎:** `pubmed_to_obsidian.py` (部署于 GitHub Actions)
- **AI 解析:** Gemini CLI (负责临床深度分析与 PICO 提取)
- **文献管理:** Zotero (自动同步至 `医学信息订阅` 分类)
- **知识库:** Obsidian (结构化笔记存入 `Papers/` 文件夹)

---

## 🚀 日常操作流程

### 1. 自动化运行 (静默模式)
- **执行时间:** 每周一 UTC 0:00 (北京时间周一上午 8 点)。
- **操作逻辑:** GitHub 会自动苏醒，抓取过去 7 天内符合条件的 **HR+/HER2-** 顶级期刊文献。
- **查看方式:** 打开 Obsidian 即可看到推送的新笔记。

### 2. 手动即时同步 (立刻获取新研究)
1. 登录 GitHub 仓库 [my-med-notes](https://github.com/Kurt-T87/my-med-notes/actions)。
2. 点击顶部导航栏 **Actions** -> **PubMed Sync**。
3. 点击右侧的 **Run workflow** -> **Run workflow**。
4. 等待 2-3 分钟，即可在本地同步查阅。

---

## 📝 笔记结构说明
每篇生成的 `.md` 笔记均包含以下高价值模块：

### ① Properties (YAML)
- **citekey / doi / pmid**: 核心元数据。
- **if**: 2025 版最新影响因子，方便筛选高分文章。
- **zotero_link**: 一键跳转至 Zotero 原始条目。

### ② 🧬 Gemini 临床深度解析 (核心价值)
- **分子亚型定位**: 快速确认是否符合你的研究方向 (如 HR+/HER2-)。
- **PICO 总结**: 结构化提取患者、干预、对照、终点。
- **临床价值**: 评价该研究是否具有“改变实践”的潜力。
- **数据亮点**: 提取关键的 HR, PFS, OS, pCR 等数值。

### ③ 📄 Abstract
- 原始摘要对照。

---

## 🔧 自定义与维护

### 修改检索关键词 (想看 TNBC 或 HER2+?)
- 打开 `pubmed_to_obsidian.py`。
- 修改第 13 行的 `SEARCH_QUERY`。
- *示例 (看 TNBC):* `SEARCH_QUERY = '("Breast Neoplasms"[Mesh]) AND ("Triple Negative")'`

### 更新期刊名单与 IF
- 在脚本的 `JOURNAL_IF_MAP` 字典中添加/修改期刊名及对应 IF。
- 脚本会自动过滤名单外的“低分杂志”。

### 环境变量 (Secrets)
如需更换 API Key，请前往 GitHub 仓库 **Settings -> Secrets and variables -> Actions** 修改：
- `ZOTERO_USER_ID`: 你的 Zotero ID。
- `ZOTERO_API_KEY`: Zotero 访问密钥。
- `GEMINI_API_KEY`: Google AI 访问密钥。

---

## 💡 进阶建议
- **Dataview 联动**: 使用 Dataview 对所有文献按 `if` 字段排序。
- **双链关联**: 建议将特定的药物（如 `[[Ribociclib]]`）或基因（如 `[[ESR1]]`）设为双链。
- **PDF 精读**: 若 Zotero 中已有 PDF，可配合 Gemini 直接进行全文解析。

---
*Created by Gemini CLI for Duan.*
