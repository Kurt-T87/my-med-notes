---
title: "Predicting neoadjuvant breast cancer therapy response using BRIDGE from tumor transcriptomics and histopathology."
journal: "Annals of oncology : official journal of the European Society for Medical Oncology"
if: 56.7
published: "2026-09-01"
doi: "10.1016/j.annonc.2026.05.700"
pmid: 42203036
zotero_link: "zotero://select/items/0_QIEPKGPU"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-09-07
---
# Predicting neoadjuvant breast cancer therapy response using BRIDGE from tumor transcriptomics and histopathology.
- **Journal**: Annals of oncology : official journal of the European Society for Medical Oncology (**IF: 56.7**)
- **Published**: 2026-09-01 | **PMID**: 42203036
- **DOI**: [10.1016/j.annonc.2026.05.700](https://doi.org/10.1016/j.annonc.2026.05.700)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_QIEPKGPU)


> [!warning] Gemini 解析失败
> Code: 55, Error: [31mGemini CLI is not running in a trusted directory. To proceed, either use `--skip-trust`, set the `GEMINI_CLI_TRUST_WORKSPACE=true` environment variable, or trust this directory in interactive mode. For more details, see https://geminicli.com/docs/cli/trusted-folders/#headless-and-automated-environments[0m


## 📄 Abstract
While expression-based signatures inform adjuvant therapy in breast cancer (BC), no approved molecular biomarkers exist for the neoadjuvant setting, where early response prediction could inform treatment decisions. This challenge is compounded by intratumoral heterogeneity, as multiple malignant subtypes may coexist within a tumor and influence therapy sensitivity.
We developed BRIDGE (BReast Intra-tumoral Deconvolution of Gene Expression), a computational framework that deconvolves the pretreatment bulk tumor transcriptome to estimate molecular subtype composition and predict pathological complete response to neoadjuvant therapy. BRIDGE was trained on 10 transcriptomics datasets and tested on 24 independent ones spanning different subtypes. Six additional datasets with pretreatment hematoxylin and eosin slides and response data were analyzed to evaluate histology-based predictions.
Analyzing measured transcriptomics, BRIDGE outperformed surrogate implementations of established commercial signatures (Oncotype DX, MammaPrint, ROR-S) in estrogen receptor (ER)-positive/human epidermal growth factor receptor 2 (HER2)-negative tumors and exceeded other transcriptomic predictors in HER2-positive and triple-negative breast cancer (TNBC) disease. In ER-positive/HER2-negative patients, it yields an receiver operating characteristic-area under the curve (AUC) of 0.84 with a high odds ratio (OR = 8); in HER2-positive disease, an AUC of 0.77 (OR = 8.3); and in TNBC, an AUC of 0.73 (OR = 3.1). We further developed BRIDGE-Slide, which applies BRIDGE to pretreatment histopathology slides via deep learning-inferred transcriptomics. BRIDGE-Slide outperforms direct slide-to-response models, underscoring its potential as a first-of-its-kind, fast, low-cost biomarker. Exploratory leave-one-dataset-out analyses across datasets treated with alternative neoadjuvant regimens suggest generalizability to immune checkpoint blockade-treated ER-positive/HER2-negative tumors, pending validation in larger cohorts. Finally, spatial transcriptomics shows that BRIDGE-derived subtype assignments form spatially cohesive regions aligned with canonical molecular features, reinforcing its biological interpretability.
BRIDGE is a biologically grounded framework for neoadjuvant BC response prediction, validated on a rich set of different patients' cohorts. Its histopathology-based version opens the door for fast and low-cost prediction in the neoadjuvant setting, upon further prospective testing and validation.
