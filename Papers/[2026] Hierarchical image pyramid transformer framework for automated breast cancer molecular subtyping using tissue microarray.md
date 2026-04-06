---
title: "Hierarchical image pyramid transformer framework for automated breast cancer molecular subtyping using tissue microarrays."
journal: "The Journal of pathology"
if: Unknown
published: "2026-04-01"
doi: "10.1002/path.70028"
pmid: 41588712
zotero_link: "zotero://select/items/0_TX9IKAQM"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-04-06
---
# Hierarchical image pyramid transformer framework for automated breast cancer molecular subtyping using tissue microarrays.
- **Journal**: The Journal of pathology (**IF: Unknown**)
- **Published**: 2026-04-01 | **PMID**: 41588712
- **DOI**: [10.1002/path.70028](https://doi.org/10.1002/path.70028)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_TX9IKAQM)


> [!info] Gemini 临床精读解析暂不可用（API 每日免费额度已耗尽）。已为你保留原始摘要供查阅。

## 📄 Abstract
The heterogeneity of breast cancer at molecular and histological levels poses significant challenges for precise diagnosis and treatment. Current molecular subtyping, crucial for guiding personalized therapy, relies on immunohistochemistry, which is often limited by intratumoral heterogeneity and potential sampling bias. While deep learning shows promise in digital pathology, existing models face computational and technical hurdles in capturing multiscale morphological features and long-range dependencies from high-resolution images, particularly in the context of tissue microarrays (TMAs). To address this, we developed and validated the pathomics breast cancer hierarchical image pyramid transformer (PBC-HIPT), a novel deep learning framework designed for automated molecular subtyping from standard H&E-stained images. The PBC-HIPT model utilizes a multilevel transformer-based architecture to hierarchically aggregate histopathological features from the cellular to the tissue scale, enabling a comprehensive analysis. We trained and validated the model on a multi-institutional cohort comprising 252 TMA cases and 46 independent whole-slide images (WSIs), assessing its performance via five-fold cross-validation on three-, four-, and five-class molecular subtyping tasks, as well as key biomarker [estrogen receptor (ER), progesterone receptor (PR), human epidermal growth factor receptor 2 (HER2), Ki-67] prediction, comparing it against several established multiple instance learning methods. PBC-HIPT demonstrated superior performance, achieving a mean accuracy of 84.3% and a mean area under the curve (AUC) of 0.91 in the clinically critical three-class subtyping task (luminal, HER2-enriched, triple-negative breast cancer), significantly outperforming baseline models. The framework excelled in biomarker prediction, attaining accuracies of 91.8% (AUC: 0.97) for ER status and 92.0% (AUC: 0.96) for PR status. It also achieved an accuracy of 73.8% (AUC: 0.81) for Ki-67 proliferation status and 84.6% (AUC: 0.85) for binary HER2 status classification. While the model showed robust intramodality generalization on TMAs (ER AUC > 0.96), its performance dropped in WSI cross-modality validation. In conclusion, the PBC-HIPT model provides a robust, automated solution for accurate molecular subtyping and biomarker assessment from H&E-stained TMAs. © 2026 The Pathological Society of Great Britain and Ireland.
