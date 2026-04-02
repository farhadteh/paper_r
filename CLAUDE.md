# Literature Review: Generative Models for Rare Disease Biomedical Data Synthesis

## Build & Environment Commands
- **Environment:** macOS
- **Document Format:** LaTeX with IEEE citations
- **Compilation:** `make build` or `pdflatex main.tex && bibtex main && pdflatex main.tex`
- **Citation Processing:** `make extract` to extract citations from `/doc` folder into `refs.bib`
- **Analysis:** R scripts in `/analysis` for synthesizing quantitative metrics

## Source Materials & Implementation Details
- **Literature Corpus:** All source papers and reference PDFs are located in the `/doc` folder. Always search and ingest documents from this directory before drafting new sections.
- **Citation Style:** IEEE format. Ensure all claims are strictly backed by the provided references.
- **Manual Bibliography:** `manuscript/refs.bib` (can be hand-edited for accuracy)
- **Context Anchoring:** The introduction and primary aim are already established. The core focus must remain continuously on the comparison between diffusion-based approaches and established methods (GANs/VAEs) specifically under the constraints of ultra-rare conditions.

## Paper Architecture & Outline
1. **Introduction** - Establishes the diagnostic odyssey of rare diseases, data scarcity constraints, and the transition from classical augmentation to deep generative models (GANs, VAEs, and Diffusion).
2. **Generative Models in Biomedical Contexts** - Technical overview comparing GANs, VAEs, and Diffusion probabilistic models in learning complex genotype-phenotype distributions.
3. **Mitigating Scarcity and Imbalance** - Evaluation of how these models specifically address limited sample sizes and class imbalance (e.g., synthesizing discrete EHRs vs. medical images).
4. **Modality-Specific Applications** - Breakdown of synthetic data generation across temporal patient data, multi-omics profiles, and medical imaging.
5. **Current Limitations** - Analysis of whether synthesized samples capture true biological variability and the privacy-preserving implications in rare disease cohorts.
6. **Conclusion & Future Directions** - Summary of challenges and next steps for clinical integration.

## Workflow

### Adding New Papers
1. Download PDF to `doc/` directory
2. Run `make extract` to regenerate `refs.bib`
3. Update `analysis/paper_metadata.csv` with paper details (title, authors, keywords, status)

### Writing Manuscript Sections
1. Edit files in `manuscript/sections/` (01-06)
2. Use IEEE citations: `\cite{author2024key}`
3. Run `make build` to compile → `manuscript/main.pdf`
4. Run `make check` to validate citations

### Full Build Pipeline
```bash
make all          # Extract + compile (full pipeline)
make quick        # Just compile (faster during active writing)
make clean        # Remove auxiliary files
make install      # Install Python dependencies
make help         # Show all available commands
```

## Writing Style & Guidelines
- **Tone:** Academic, highly objective, and analytical
- **Synthesis over Summary:** Do not just list what each paper did. Synthesize the findings to answer the core research question of *how* these models are addressing data scarcity
- **Active Voice:** "Researchers applied..." not "It was applied..."
- **Strict Citation Backing:** Every claim needs `\cite{}`
- **Vocabulary Constraint - Prohibited Phrases:**
  - "It is crucial to note"
  - "Delving into"
  - "It is worth noting"
  - "Furthermore"
  - "Moreover"
  - "In conclusion" (use "We conclude that..." instead)
  - "It should be noted that"
- **Use active voice** to describe research actions

## Dependencies
- **LaTeX:** BasicTeX/MacTeX with IEEEtran package
  - Install: `brew install --cask basictex`
  - Add to PATH: `export PATH="/Library/TeX/texbin:$PATH"`
  - Install packages: `sudo tlmgr update --self && sudo tlmgr install IEEEtran`
- **Python:** pypdf, pdfplumber, bibtexparser, pandas, requests
  - Install: `make install`
- **R (optional):** tidyverse, knitr, xtable for quantitative analysis

## Build Commands Reference
- `make help` - Show all available commands
- `make install` - Install Python dependencies
- `make extract` - Extract citations from PDFs → refs.bib
- `make build` - Compile manuscript → main.pdf
- `make check` - Validate all citations
- `make clean` - Remove build artifacts
- `make quick` - Fast build without citation extraction
- `make all` - Full pipeline (extract + build)

## Project Structure
```
paper_r/
├── doc/                     # PDF papers (7 papers)
├── manuscript/              # LaTeX manuscript
│   ├── main.tex            # Main document
│   ├── refs.bib            # Bibliography
│   ├── sections/           # Section files (01-06)
│   ├── figures/            # Figures
│   └── tables/             # Generated tables
├── scripts/                 # Automation scripts
│   ├── build_manuscript.sh # LaTeX build script
│   ├── parse_refs.py       # Citation extractor
│   ├── validate_citations.py # Citation checker
│   └── check_style.py      # Style/quality checker
├── analysis/                # R scripts and data
│   └── paper_metadata.csv  # Paper tracking
├── Makefile                 # Build automation
├── requirements.txt         # Python dependencies
├── CLAUDE.md               # This file
└── README.md               # Project documentation
```

## Notes
- LaTeX compilation requires 3 passes for citations: `pdflatex → bibtex → pdflatex → pdflatex`
- IEEE citation style uses numbered references [1], [2], etc.
- All writing should be in section files under `manuscript/sections/`, not in `main.tex`
- Use `make quick` during active writing to avoid slow citation extraction
- PDF extraction may fail for some papers (encryption, OCR-only) - manual bibliography in `refs.bib` is the fallback
