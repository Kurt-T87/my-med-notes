---
title: "A machine learning assay to predict disease recurrence in hormone receptor-positive breast cancer."
journal: "ESMO open"
if: Unknown
published: "2026-03-01"
doi: "10.1016/j.esmoop.2026.106064"
pmid: 41895875
zotero_link: "zotero://select/items/0_ASIQR53J"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-03-30
---
# A machine learning assay to predict disease recurrence in hormone receptor-positive breast cancer.
- **Journal**: ESMO open (**IF: Unknown**)
- **Published**: 2026-03-01 | **PMID**: 41895875
- **DOI**: [10.1016/j.esmoop.2026.106064](https://doi.org/10.1016/j.esmoop.2026.106064)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_ASIQR53J)

这份关于 **ER-Predict** 机器学习分析的研究为 HR+/HER2- 早期乳腺癌的精准复发风险评估提供了新的视角。以下是基于转化医学与临床维度的深度解析：

## 🧬 Gemini 临床深度解析

- **分型与人群:** 
  **HR+/HER2-（激素受体阳性、人表皮生长因子受体 2 阴性）早期乳腺癌**。该人群具有特征性的“长尾效应”，即在术后多年仍面临持续的复发风险。

- **PICO 核心:** 
    - **P (Patient):** 早期 HR+/HER2- 乳腺癌患者（开发集 n=1413，外部验证集 n=1118）。
    - **I (Intervention):** 基于机器学习开发的 **ER-Predict**（14 基因表达特征分析）。
    - **C (Comparison):** 传统临床病理因素（分级、肿瘤大小、淋巴结状态）以及再现的经典多基因模型（如 Oncotype DX, EndoPredict）。
    - **O (Outcome):** 核心终点为**远处无转移生存期 (DMFS)**；次要终点包括独立预后价值验证及功能注释。

- **临床价值:** 
    - **识别“临床低危但基因高危”患者：** 该研究最核心的价值在于其能够突破传统临床指标的局限，精准识别出那些看似低危（如小肿瘤、无淋巴结转移）但生物学行为活跃、极易发生远程转移的患者。
    - **指导强化治疗方案：** 随着 CDK4/6 抑制剂（如阿贝西利、瑞波西利）进入辅助治疗，ER-Predict 可作为决策支持工具，帮助筛选哪些患者需要叠加细胞周期抑制剂，而非单纯行内分泌治疗。
    - **药理靶向提示：** 研究揭示了高危肿瘤中 RB1 表达保留且细胞周期调节因子激活，这为临床应用 CDK4/6i 提供了理论上的“行动力（Actionability）”依据。

- **关键数据:** 
    - **风险预测效能：** 外部验证集中，ER-Predict 识别的高危组 DMFS 显著缩短，**HR 为 2.03** (95% CI 1.57-2.63, P < 0.0001)。
    - **独立预后因子：** 经多因素回归分析，ER-Predict 的预后价值独立于肿瘤大小、分级及淋巴结状态。
    - **优越性评估：** 在同口径对比中，ER-Predict 的表现优于重新计算的传统多基因面板（MGAs）。

- **专家评述:** 
    - **研究亮点：** ER-Predict 结合了机器学习算法与基因表达特征，相比于早期的线性模型，能更好地捕获基因间的非线性相互作用，提高了在 Luminal 型肿瘤中的特异性。
    - **潜在局限与偏倚：** 
        1.  **回顾性数据依赖：** 外部验证主要基于公开数据库（Publicly available cohorts），这类数据往往存在治疗方案不统一、随访质量参差不齐的问题。
        2.  **“黑盒”属性：** 尽管明确了 14 个基因，但机器学习算法的内部逻辑在临床解释上往往不如 Oncotype DX 那样直观。
    - **后续关注点：** 亟需前瞻性临床试验（如类似于 TAILORx 或 MINDACT 级别的研究）来验证 ER-Predict 指导下的升阶/降阶治疗是否能真正改善患者的总生存期（OS），特别是其在指导辅助 CDK4/6 抑制剂使用上的前瞻性获益。

## 📄 Abstract
Hormone receptor (HR)-positive, human epidermal growth factor 2 (HER2)-negative breast cancer associates with a sustained risk of relapse over time. Current multigene assays offer limited validity to identify clinically low-risk tumors at high risk of recurrence, which is particularly relevant in the context of novel adjuvant therapies. In this study, we developed and validated ER-Predict, a machine learning assay leveraging a 14-gene expression signature to classify early stage HR-positive/HER2-negative breast cancer according to the risk of relapse.
ER-Predict was developed on a cohort of 1413 HR-positive/HER2-negative early breast cancer cases. External validation was carried out across eight publicly available cohorts (n = 1118). Comparative benchmarking was conducted against reproduced prognostic signatures, and particularly, EndoPredict and Oncotype DX. Functional annotation and drug response analysis were carried out using gene expression and pharmacogenomic data from publicly available breast cancer cell lines.
ER-Predict identified high-risk patients with significantly reduced distant metastasis-free survival in the external validation cohort (hazard ratio 2.03, 95% confidence interval 1.57-2.63, P < 0.0001). The assay demonstrated independent prognostic value beyond traditional clinicopathological factors, including tumor grade, tumor size, and nodal status, and consistently outperformed recomputed multigene panels. ER-Predict showed specificity toward luminal-like transcriptomic programs, revealing activation of key cell-cycle regulators governing endocrine resistance among high-risk tumors that had retained expression of retinoblastoma-1, suggesting potential actionability by means of cell-cycle inhibitors.
ER-Predict represents a robust assay with potential utility in early stage HR-positive/HER2-negative breast cancer. Its consistent ability to identify high-risk patients supports further investigation as a decision-support tool to guide treatment intensification in clinically low-risk HR-positive/HER2-negative disease.
