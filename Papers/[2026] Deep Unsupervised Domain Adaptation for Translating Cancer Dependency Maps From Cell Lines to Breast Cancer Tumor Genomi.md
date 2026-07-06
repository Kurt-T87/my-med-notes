---
title: "Deep Unsupervised Domain Adaptation for Translating Cancer Dependency Maps From Cell Lines to Breast Cancer Tumor Genomics."
journal: "Genetic epidemiology"
if: Unknown
published: "2026-07-01"
doi: "10.1002/gepi.70044"
pmid: 42339999
zotero_link: "zotero://select/items/0_VPRH4294"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-07-06
---
# Deep Unsupervised Domain Adaptation for Translating Cancer Dependency Maps From Cell Lines to Breast Cancer Tumor Genomics.
- **Journal**: Genetic epidemiology (**IF: Unknown**)
- **Published**: 2026-07-01 | **PMID**: 42339999
- **DOI**: [10.1002/gepi.70044](https://doi.org/10.1002/gepi.70044)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_VPRH4294)


> [!warning] Gemini 解析失败
> Code: 55, Error: [31mGemini CLI is not running in a trusted directory. To proceed, either use `--skip-trust`, set the `GEMINI_CLI_TRUST_WORKSPACE=true` environment variable, or trust this directory in interactive mode. For more details, see https://geminicli.com/docs/cli/trusted-folders/#headless-and-automated-environments[0m


## 📄 Abstract
The Cancer dependency maps (DepMap) identify genetic dependencies in cancer cells using large-scale loss-of-function screens, providing a foundation for cancer-specific treatment strategies. However, discrepancies exist between cancer cell line models (CCLs) and patient-derived tumor models, particularly in translating findings to clinical settings. To bridge this gap, computational approaches such as artificial intelligence-based domain adaptation can assist in aligning laboratory and patient-derived molecular data, thereby improving the translation of preclinical findings into personalized treatment strategies. We developed a deep unsupervised domain adaptation (UDA) algorithm to align features between source and target domains. It was trained on labeled CCLs data from the source domain and unseen, unlabeled CCL data from the target domain. The trained model was applied to predict the dependency map of breast cancer (BC) patients in The Cancer Genome Atlas (TCGA). To validate its performance, we used the predicted BC dependency map to classify ER + /HER2 + BC subtype statuses and identify synthetic lethality (SL) gene pairs for drug discovery. Our model demonstrated high accuracy in predicting cancer dependency maps for patient-derived tumors. The generated maps showed excellent performance in predicting ER + /HER2+ subtype statuses, with an area under the curve of the receiver operating characteristic (AUC-ROC) of 0.99. Notably, our analysis also identified two potential synthetic lethality gene pairs: PBRM1-NF2 and PBRM1-CTNND2, which can be potentially used for developing precision therapies for ER + /HER2+ breast cancer. Domain adaptation is a promising approach for transferring biological knowledge between different cancer models and improving patient-specific treatment strategies.
