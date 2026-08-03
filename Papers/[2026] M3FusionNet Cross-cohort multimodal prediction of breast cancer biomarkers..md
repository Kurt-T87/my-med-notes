---
title: "M3FusionNet: Cross-cohort multimodal prediction of breast cancer biomarkers."
journal: "Computational biology and chemistry"
if: Unknown
published: "2026-10-01"
doi: "10.1016/j.compbiolchem.2026.109228"
pmid: 42407417
zotero_link: "zotero://select/items/0_D99IDZ9A"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-08-03
---
# M3FusionNet: Cross-cohort multimodal prediction of breast cancer biomarkers.
- **Journal**: Computational biology and chemistry (**IF: Unknown**)
- **Published**: 2026-10-01 | **PMID**: 42407417
- **DOI**: [10.1016/j.compbiolchem.2026.109228](https://doi.org/10.1016/j.compbiolchem.2026.109228)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_D99IDZ9A)


> [!warning] Gemini 解析失败
> Code: 55, Error: [31mGemini CLI is not running in a trusted directory. To proceed, either use `--skip-trust`, set the `GEMINI_CLI_TRUST_WORKSPACE=true` environment variable, or trust this directory in interactive mode. For more details, see https://geminicli.com/docs/cli/trusted-folders/#headless-and-automated-environments[0m


## 📄 Abstract
Accurate prediction of breast cancer biomarkers - including oestrogen receptor (ER), progesterone receptor (PR), human epidermal growth factor receptor 2 (HER2), molecular subtypes (PAM50), and the proliferation marker Ki-67 (MKI67) - is essential for treatment stratification and prognosis. Existing computational approaches predominantly rely on single-cohort data, limiting their clinical generalisability.
We propose M3FusionNet (Multi-modal, Multi-scale, Multi-source Fusion Network), a comprehensive multimodal deep learning framework integrating haematoxylin-and-eosin (H&E) whole slide images (WSIs), RNA-seq, miRNA, proteomics, and clinical variables for simultaneous prediction of five breast cancer biomarkers. Feature extraction from WSIs was performed using ResNet50 (2,048-dimensional embeddings), with subsequent feature-level fusion across modalities. Gradient-boosted models (XGBoost, CatBoost) were employed for both classification (ER, PR, HER2, PAM50) and continuous regression (MKI67). Crucially, M3FusionNet is evaluated through three experimental protocols spanning TCGA-BRCA n ≈ 1036) and CPTAC-BRCA (n ≈ 134), with comprehensive domain adaptation via Macenko stain normalisation and ComBat batch correction.
In-distribution performance on TCGA reached AUC values of 0.99 (ER), 0.96 (PR), 0.98 (HER2), and 0.96 (PAM50 macro-AUC), with an overall AUC of 0.97. Cross-dataset generalisation exhibited a controlled 13-22% AUC reduction (E1: Overall AUC 0.82), substantially mitigated by harmonised preprocessing and multimodal fusion. The combined TCGA + CPTAC model (M3FusionNet-E3) demonstrated superior robustness with Overall AUC of 0.90, particularly for HER2-enriched and triple-negative subtypes. Proteomics integration (CPTAC-exclusive) improved HER2 AUC by 2-3 %age points.
M3FusionNet establishes one of the first comprehensive cross-cohort multimodal evaluation framework for breast cancer biomarker prediction, demonstrating that proteogenomic integration and domain-adapted fusion substantially improve generalisation. The protein-level Ki-67 regression from CPTAC mass spectrometry data constitutes a novel, clinically meaningful regression target. M3FusionNet offers a scalable pathway towards robust, multimodal computational pathology applicable across diverse clinical settings.
