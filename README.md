# Cancer Genomics: Mutational Signature Comparison — LUAD vs COAD

Comparative analysis of SBS mutational signatures between Lung Adenocarcinoma 
(LUAD) and Colorectal Adenocarcinoma (COAD) using public TCGA somatic mutation 
data and open-source bioinformatics tools.

Internship Project | June 2026  
Nilesh Ghosh | St. Xavier's College, Burdwan

---

## Project Overview

This project compares the mutational signature landscapes of two cancer types —
LUAD (lung) and COAD (colorectal) — to identify cancer-type-specific and shared 
mutagenic processes. SBS96 trinucleotide mutation matrices were constructed from 
TCGA MAF files and decomposed into de novo signatures using Non-negative Matrix 
Factorization (NMF), then matched against the COSMIC SBS v3.5 reference library.

---

## Data Source

- Platform: TCGA GDC Data Portal (https://portal.gdc.cancer.gov)
- File type: Masked somatic mutation MAF files (.maf.gz)
- LUAD cohort: 531 samples
- COAD cohort: 343 samples
- Reference genome: GRCh38
- Note: Pre-processed pipeline-standardized MAF files were used directly;
  raw FASTQ processing and variant calling were not performed.

---

## Tools & Environment

| Tool | Version | Purpose |
|---|---|---|
| R | 4.x | Statistical analysis and visualisation |
| maftools | Bioconductor | Mutation landscape, oncoplots, mafCompare |
| ggplot2 | 3.x | Comparative signature bar plots |
| SigProfilerMatrixGenerator | Python/WSL | SBS96 mutation matrix construction |
| SigProfilerExtractor | Python/WSL | De novo NMF signature extraction |
| COSMIC SBS | v3.5 | Reference signature matching |
| OS | Ubuntu (WSL2) | Runtime environment for Python tools |

---

## Pipeline

1. Download masked somatic MAF files from TCGA GDC portal
2. Load and explore mutation landscape per cohort using maftools in R
3. Generate SBS96 trinucleotide mutation matrices using SigProfilerMatrixGenerator
4. Extract de novo signatures independently per cohort using SigProfilerExtractor (NMF)
5. Match de novo signatures to COSMIC SBS v3.5 reference via cosine similarity
6. Compare proportional signature contributions between LUAD and COAD using ggplot2

---

## SigProfilerExtractor Parameters

| Parameter | Value |
|---|---|
| Input type | Matrix (SBS96) |
| Reference genome | GRCh38 |
| COSMIC version | v3.5 |
| Signature range | 1–10 |
| NMF replicates | 10 |
| CPU cores | 2 |
| Optimal solution — LUAD | 3 signatures |
| Optimal solution — COAD | 4 signatures |

---

## Key Findings

### LUAD (531 samples)

| De Novo Sig | COSMIC Match | Cosine Similarity | Dominant Process |
|---|---|---|---|
| SBS96A | SBS4 (92.9%), SBS5 (6.86%) | 0.978 | Tobacco/PAH exposure |
| SBS96B | SBS13 (41.5%), SBS2 (39.6%), SBS5 (16%) | 0.991 | APOBEC deaminase activity |
| SBS96C | SBS5 (63.8%), SBS6 (23.8%), SBS51 (12.4%) | 0.959 | Clock-like / MMR deficiency |

Cohort-level dominant process: **SBS4 — tobacco carcinogenesis (61.8% of mutations)**

### COAD (343 samples)

| De Novo Sig | COSMIC Match | Cosine Similarity | Dominant Process |
|---|---|---|---|
| SBS96A | SBS15 (38.2%), SBS20 (22.9%), SBS5 (18.7%) | 0.970 | MMR deficiency / MSI |
| SBS96B | SBS10b (48.7%), SBS10a (33.7%), SBS15 (17.6%) | 0.991 | POLE ultramutator |
| SBS96C | SBS1 (66.2%), SBS15 (31.6%), SBS5 (2.2%) | 0.969 | Age-related CpG deamination |
| SBS96D | SBS40a (70.2%), SBS1 (23%), SBS5 (6.7%) | 0.913 ⚠️ low confidence | Unknown endogenous process |

### Comparison Summary

| Signature | LUAD | COAD | Biological Meaning |
|---|---|---|---|
| SBS4 | ✅ dominant | ❌ absent | Tobacco exposure |
| SBS2/SBS13 | ✅ present | ❌ absent | APOBEC mutagenesis |
| SBS10a/10b | ❌ absent | ✅ present | POLE dysfunction |
| SBS15/SBS20 | minor | ✅ present | MMR deficiency / MSI |
| SBS1/SBS5 | ✅ present | ✅ present | Universal aging signatures |
