---
title: "A mechanistic learning framework for breast cancer relapse prediction."
journal: "Mathematical biosciences"
if: Unknown
published: "2026-12-01"
doi: "10.1016/j.mbs.2026.109830"
pmid: 42892345
zotero_link: "zotero://select/items/0_CC8Q7X6A"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-11-16
---
# A mechanistic learning framework for breast cancer relapse prediction.
- **Journal**: Mathematical biosciences (**IF: Unknown**)
- **Published**: 2026-12-01 | **PMID**: 42892345
- **DOI**: [10.1016/j.mbs.2026.109830](https://doi.org/10.1016/j.mbs.2026.109830)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_CC8Q7X6A)


> [!warning] Gemini 解析失败
> Code: 55, Error: [31mGemini CLI is not running in a trusted directory. To proceed, either use `--skip-trust`, set the `GEMINI_CLI_TRUST_WORKSPACE=true` environment variable, or trust this directory in interactive mode. For more details, see https://geminicli.com/docs/cli/trusted-folders/#headless-and-automated-environments[0m


## 📄 Abstract
Breast cancer recurrence is thought to arise, at least in part, from disseminated tumour cells (DTCs) that may seed distant organs prior to or during surgery, persist in a dormant state for years to decades, and eventually resume proliferation to form clinically detectable metastases. Standard survival models treat this process statistically, without reference to the underlying biological kinetics, and while artificial intelligence (AI) has improved predictive accuracy, its "black-box" nature limits clinical interpretability. Here we present a mechanistic learning approach that relates routine histopathological data to a mathematical model of tumour growth. Three modular buckets assign clinical observables to latent kinetic parameters: Seed (initial metastatic burden), Speed (effective proliferative rate), and Soil (permissiveness of the tumour microenvironment), guided by pathology expertise within the author team. In the METABRIC cohort (1,814 patients, 737 relapses) we implement Seed with tumour size and lymph node count, and Speed with histological grade and ER, HER2, and PR status. Soil is designed for stromal tumour-infiltrating lymphocyte scores and PD-L1 expression, which this cohort does not record. Feature-selection experiments on the same data examined tumour cellularity, age, and RNA-based immune proxies as candidate Soil variables, but the bucket is reserved for datasets that record these variables directly. The model estimates a patient-level initial DTC burden and covariate-associated deviations in proliferative rate, which enter an exponential growth model to yield a patient-specific predicted relapse time. Anchoring the model to a literature-based reference phenotype ensures parameter identifiability and fixes the absolute scale of these quantities. A saturating (logarithmic) link between lymph-node involvement and initial metastatic burden keeps the predicted relapse time positive for 99.8% of patients, and a bounded link, examined as a sensitivity analysis, does so for all. Fitted with a censoring-aware loss and evaluated by internal five-fold cross-validation on this cohort, the model attains a concordance index (a measure of how well predicted relapse times rank the observed survival times) of 0.654, comparable to a multivariate Cox proportional-hazards baseline, while each prediction decomposes into an initial tumour burden and a proliferative rate that trace back to routine histopathological measurements. This proof of concept provides a modular foundation for future multi-centre mathematical-oncology research.
