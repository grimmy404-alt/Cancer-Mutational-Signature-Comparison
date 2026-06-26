
# Cancer Genomics: Mutational Signature Comparison — LUAD vs COAD

Comparative analysis of SBS mutational signatures between Lung Adenocarcinoma (LUAD) and Colorectal Adenocarcinoma (COAD) using TCGA public data.

## Data Source

- TCGA GDC Portal: https://portal.gdc.cancer.gov
- LUAD cohort: 531 samples
- COAD cohort: 343 samples
- Reference genome: GRCh38

## Tools & Environment

| Tool | Purpose |
|------|---------|
| maftools (R) | Mutation landscape, oncoplots, gene summaries |
| SigProfilerMatrixGenerator (Python) | SBS96 mutation matrix construction |
| SigProfilerExtractor (Python) | De novo signature extraction via NMF |
| COSMIC v3.3 | Reference signature annotation |
| WSL2 / Ubuntu | Runtime environment |

## Workflow

1. Download MAF files from TCGA GDC portal
2. Explore mutation landscape with maftools
3. Generate SBS96 matrices with SigProfilerMatrixGenerator
4. Extract de novo signatures with SigProfilerExtractor
5. Map de novo signatures to COSMIC SBS reference via cosine similarity
6. Compare signature contributions between cohorts

## Key Findings

**LUAD — 3 signatures**
| Signature | Etiology | Contribution |
|-----------|----------|-------------|
| SBS4 | Tobacco/BPDE — C>A transversions | ~46% |
| SBS5 | Clock-like, unknown etiology | ~33% |
| SBS2+SBS13 | APOBEC cytidine deaminase activity | ~11% |

**COAD — 4 signatures**
| Signature | Etiology | Contribution |
|-----------|----------|-------------|
| SBS1 | Age-related CpG deamination | ~40% |
| SBS5 | Clock-like, unknown etiology | ~28% |
| SBS15+SBS20 | Mismatch repair deficiency | ~11% |
| SBS10a+SBS10b | POLE ultramutator phenotype | ~3.5% |

**Shared:** SBS5 present in both cohorts  
**LUAD-unique:** SBS4 (tobacco), SBS2/SBS13 (APOBEC)  
**COAD-unique:** SBS1 (aging), SBS15/SBS20 (MMR deficiency), SBS10a/b (POLE)
