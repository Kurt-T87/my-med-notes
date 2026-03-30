---
title: "Analysis of Large Language Model Decision Making in Hormone Receptor-Positive/Human Epidermal Growth Factor Receptor 2-Negative Early Breast Cancer."
journal: "JCO clinical cancer informatics"
if: Unknown
published: "2026-03-01"
doi: "10.1200/CCI-25-00230"
pmid: 41791000
zotero_link: "zotero://select/items/0_NQPAFHGT"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-03-30
---
# Analysis of Large Language Model Decision Making in Hormone Receptor-Positive/Human Epidermal Growth Factor Receptor 2-Negative Early Breast Cancer.
- **Journal**: JCO clinical cancer informatics (**IF: Unknown**)
- **Published**: 2026-03-01 | **PMID**: 41791000
- **DOI**: [10.1200/CCI-25-00230](https://doi.org/10.1200/CCI-25-00230)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_NQPAFHGT)

这份研究聚焦于人工智能（AI）在乳腺癌辅助治疗决策中的表现。以下是基于文献摘要的临床深度解析：

## 🧬 Gemini 临床深度解析

- **分型与人群:** 
    - **HR+/HER2- 早期乳腺癌**（HR-positive/HER2-negative early breast cancer）。
    - 涉及两个队列：队列 1 (C1, n=607) 为常规临床实践人群；队列 2 (C2, n=237) 为前瞻性多中心 PRO BONO 研究人群。

- **PICO 核心:** 
    - **P (Patient):** 已进行 Oncotype DX（21 基因）检测的 HR+/HER2- 早期乳腺癌患者。
    - **I (Intervention):** GPT-4o 大语言模型给出的辅助治疗建议（化疗+内分泌治疗 [CT+ET] vs. 单纯内分泌治疗 [ET]）。
    - **C (Comparison):** 临床医生的实际治疗建议/决策。
    - **O (Outcome):** 核心指标为 GPT-4o 与医生建议之间的一致性（Agreement rates & Cohen's kappa）以及预测基因风险的准确性（AUC）。

- **临床价值:** 
    - 该研究验证了 AI 在辅助治疗决策支持方面的潜力，但**并未挑战现有指南**，反而强调了**多基因检测（如 Oncotype DX）对于精准医疗的不可替代性**。
    - 结果显示，当缺乏客观基因证据时，AI 与医生的分歧较大；一旦加入基因检测数据，AI 的判断与人类专家高度趋同。这提示 LLM 可作为临床医生的“第二意见”工具，辅助解读复杂检测结果。

- **关键数据:** 
    - **一致性提升:** 在获得基因检测结果前（Pre-test），GPT-4o 与医生的一致性仅为 **68-70%**（Kappa 0.38-0.40，中等一致性）；获得结果后（Post-test），一致性大幅升至 **90-93%**（Kappa 0.74-0.81，高度一致）。
    - **治疗倾向:** 在 Pre-test 阶段，**医生比 GPT-4o 更“激进”**。医生推荐化疗的比例（53-58%）显著高于 GPT-4o（38-43%）。
    - **风险预测偏倚:** GPT-4o 预测“低基因风险”的准确性很高（绝经后约 **85-87%**），但预测“高基因风险”的准确性极差（仅 **43-45%**）。

- **专家评述:** 
    - **潜在偏倚:** GPT-4o 表现出明显的“保守偏倚”，在缺乏基因数据时倾向于低估化疗的必要性（Under-treatment 风险）。尤其是其对“高基因风险”预测的低准确率（<50%），意味着**目前阶段 AI 绝不能脱离医生监控独立决策**，否则可能导致高复发风险患者漏掉化疗。
    - **后续关注点:** 
        1. **黑盒效应:** 需进一步探究 AI 决策的逻辑依据（例如它是更看重肿瘤大小还是 Ki-67？）。
        2. **指南时效性:** GPT-4o 的训练数据截止日期可能影响其对最新临床试验（如 RxPONDER 对绝经前人群的细化建议）的解读。
        3. **前瞻性验证:** 需要更多像 PRO BONO 这样的研究来验证 AI 在真实世界、不同医疗资源背景下的鲁棒性。

## 📄 Abstract
To assess the ability of GPT-4o in adjuvant treatment decision making in hormone receptor-positive (HR+)/human epidermal growth factor receptor 2-negative (HER2-) early breast cancer by comparing its recommendations with those of clinicians including Oncotype DX data, and to explore its potential as a decision-support tool in routine clinical practice.
We compared clinician and GPT-4o recommendations in patients tested with Oncotype DX in routine practice at the University of Naples Federico II (n = 607, cohort 1 [C1]) and within the prospective, multicenter PRO BONO study (n = 237, cohort 2 [C2]). Pre- and post-Oncotype DX treatment recommendations were categorized as chemotherapy (CT) + endocrine therapy (ET) or ET alone. Concordance between clinician and GPT-4o recommendations was assessed using agreement rates and Cohen's kappa. The accuracy of Oncotype DX results was evaluated using the AUC metric.
The agreement between clinicians and GPT-4o in pretest recommendations was 68% (kappa, 0.381 [95% CI, 0.31 to 0.45], <i>P</i> < .001) in C1 and 70% (0.401 [95% CI, 0.29 to 0.52], <i>P</i> < .001) in C2. Before Oncotype DX, clinicians recommended CT more frequently than GPT-4o for C1 (58% <i>v</i> 38%) and C2 (53% <i>v</i> 43%). Post-test agreement increased to 93% (0.814 [95% CI, 0.76 to 0.87], <i>P</i> < .001) in C1 and 90% (0.741 [95% CI, 0.64 to 0.84], <i>P</i> < .001) in C2. The agreement between pre- and post-Oncotype DX treatment recommendations for clinicians was 56% and 63% versus 68% and 60% for GPT-4o in C1 and C2, respectively. GPT-4o showed higher accuracy in predicting low than high genomic risk in postmenopausal patients (87% <i>v</i> 43% in C1; 85% <i>v</i> 45% in C2, <i>P</i> < .001) and low versus intermediate and high risk in premenopausal patients in both cohorts (<i>P</i> < .001).
The agreement between clinicians and GPT-4o in pretest recommendations was modest but improved post-test, highlighting the importance of multigene testing and the potential of large language models in clinical decision making.
