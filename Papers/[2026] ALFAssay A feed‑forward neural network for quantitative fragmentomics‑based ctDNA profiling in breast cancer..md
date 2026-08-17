---
title: "ALFAssay: A feed‑forward neural network for quantitative fragmentomics‑based ctDNA profiling in breast cancer."
journal: "PLoS computational biology"
if: Unknown
published: "2026-07-01"
doi: "10.1371/journal.pcbi.1014505"
pmid: 42507708
zotero_link: "zotero://select/items/0_SIIXVE2S"
tags: #BC #HR+HER2- #GeminiAnalyzed
sync_date: 2026-08-17
---
# ALFAssay: A feed‑forward neural network for quantitative fragmentomics‑based ctDNA profiling in breast cancer.
- **Journal**: PLoS computational biology (**IF: Unknown**)
- **Published**: 2026-07-01 | **PMID**: 42507708
- **DOI**: [10.1371/journal.pcbi.1014505](https://doi.org/10.1371/journal.pcbi.1014505)
- **Zotero**: [点击跳转 Zotero 库](zotero://select/items/0_SIIXVE2S)


> [!warning] Gemini 解析失败
> Code: 55, Error: [31mGemini CLI is not running in a trusted directory. To proceed, either use `--skip-trust`, set the `GEMINI_CLI_TRUST_WORKSPACE=true` environment variable, or trust this directory in interactive mode. For more details, see https://geminicli.com/docs/cli/trusted-folders/#headless-and-automated-environments[0m


## 📄 Abstract
The analysis of cell‑free DNA (cfDNA) is transforming cancer diagnostics, yet quantifying the fraction of circulating tumour DNA (ctDNA) from shallow whole‑genome sequencing (sWGS) remains challenging in tumours with low copy‑number aberration burden. We introduce ALFAssay, a feed‑forward neural network that estimates ctDNA fraction from fragmentation profiles of cfDNA in breast cancer. Using cfDNA from 896 plasma samples spanning early and metastatic HR + /HER2- and triple‑negative breast cancer, and healthy controls, (id: NCT03616886, NCT02028364, NCT03065621) we extract 204 bin‑level fragmentation features by computing the ratio of short fragments (90-150 bp) to all reads within 5 Mb genomic windows, while accounting for coverage effects by incorporating the total number of reads for each bin as an additional input feature. The resulting 408‑dimensional vectors are input to a fully connected network trained against ichorCNA‑derived ctDNA fractions using five‑fold cross‑validation. ALFAssay demonstrates high sensitivity (0.87) and specificity (0.94) for ctDNA detection and correlates with ichorCNA (r = 0.89) and the fragmentation‑based tool Fragle (r = 0.81). Its ctDNA predictions stratify patients by progression‑free survival and add complementary prognostic value to available tools. ALFAssay thus expands the bioinformatics toolkit for ctDNA quantification and highlights the potential of fragmentation signatures to augment multi‑modal liquid‑biopsy workflows.
