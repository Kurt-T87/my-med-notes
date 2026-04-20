---
title: "Predicting the Efficacy of Breast Cancer Neoadjuvant Chemotherapy Using Ultrasonography and Machine Learning."
journal: "Ultrasound in medicine & biology"
if: 12.8
published: "2026-04-01"
doi: "10.1016/j.ultrasmedbio.2025.12.009"
pmid: 41580311
zotero_link: "zotero://select/items/0_6P4MGHE8"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-04-20
---
# Predicting the Efficacy of Breast Cancer Neoadjuvant Chemotherapy Using Ultrasonography and Machine Learning.
- **Journal**: Ultrasound in medicine & biology (**IF: 12.8**)
- **Published**: 2026-04-01 | **PMID**: 41580311
- **DOI**: [10.1016/j.ultrasmedbio.2025.12.009](https://doi.org/10.1016/j.ultrasmedbio.2025.12.009)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_6P4MGHE8)


> [!info] Gemini 临床精读解析暂不可用（API 每日免费额度已耗尽）。已为你保留原始摘要供查阅。

## 📄 Abstract
This study aimed to develop a machine learning model based on ultrasonography (US) and clinicopathological features to predict pathological complete response (pCR) following neoadjuvant chemotherapy (NAC) in patients with breast cancer. The goal was to establish a non-invasive prediction tool to facilitate individualized treatment planning.
A retrospective analysis was conducted on data from 463 patients with breast cancer who underwent NAC at Shanxi Bethune Hospital between January 2018 and December 2024. Patients were randomly allocated into a training set (n = 277) and a test set (n = 118). To address class imbalance, the Synthetic Minority Over-sampling Technique algorithm was applied. Ten key features, including tumor short diameter, maximum elasticity, and age group, were selected through Least Absolute Shrinkage and Selection Operator regression. Seven machine learning models were constructed, including Random Forest, Logistic Regression, and Extreme Gradient Boosting (XGBoost). Model parameters were optimized through ten-fold cross-validation. Performance evaluation involved receiver operating characteristic (ROC) curves, decision curve analysis (DCA), and calibration curves.
Among the developed models, XGBoost demonstrated superior performance, achieving an area under the ROC curve of 0.8955 (95% confidence interval: 0.8409-0.9601), sensitivity of 0.8095, and specificity of 0.8026 in the test set. Shapley Additive Explanations analysis identified ER-negative, PR-negative, tumor short diameter, and HER2-positive as significant predictors of pCR (contribution > 15%). DCA indicated that XGBoost provided the highest net benefit within clinical decision thresholds (10%-90%), and the calibration curve demonstrated good consistency between predicted and observed outcomes, with a slope approaching 1 (Brier score = 0.11).
The XGBoost model, incorporating US imaging and clinicopathological features, demonstrated high accuracy in predicting pCR following NAC in patients with breast cancer. These findings indicate that the model may serve as a valuable tool for efficacy evaluation. Further validation with multi-center data is necessary to confirm generalizability and support clinical application.
