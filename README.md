# Literature Review Pipeline: Generative Models for Rare Disease Biomedical Data Synthesis

A complete automated pipeline for writing an academic literature review using LaTeX, with citation management, build automation, and quality checks.

## Quick Start

```bash
# 1. Install dependencies
make install

# 2. Build the manuscript
make build

# 3. View the PDF
open manuscript/main.pdf
```

---

## 💻 Working from Another Computer

This repository is hosted on GitHub at: **<https://github.com/farhadteh/paper_r>**

### Clone the Repository

```bash
git clone https://github.com/farhadteh/paper_r.git
cd paper_r
```

### Setup on New Computer

Follow the installation steps below, then:

```bash
# 1. Install dependencies
make install

# 2. Build the manuscript
make build

# 3. View the PDF
open manuscript/main.pdf
```

### Making Changes and Syncing

**After editing on any computer:**

```bash
# Build to verify your changes
make build

# Stage your changes
git add manuscript/sections/01_introduction.tex
# Or stage all changes: git add .

# Commit with a descriptive message
git commit -m "Updated introduction section"

# Push to GitHub
git push
```

**Before starting work (pull latest changes):**

```bash
git pull
```

This ensures you always have the latest version from any computer.

---

## Installation

### 1. LaTeX Distribution

Install BasicTeX (lightweight) or MacTeX (full):

```bash
# Option A: BasicTeX (recommended, ~100MB)
brew install --cask basictex

# Option B: MacTeX (full distribution, ~4GB)
brew install --cask mactex-no-gui
```

After installation, add TeX to your PATH and install IEEE packages:

```bash
# Add to PATH
export PATH="/Library/TeX/texbin:$PATH"

# Update tlmgr and install packages
sudo tlmgr update --self
sudo tlmgr install IEEEtran bibtex
```

Add the PATH export to your shell profile (`.zshrc` or `.bash_profile`) to make it permanent.

### 2. Python Dependencies

The virtual environment is already created. Install packages:

```bash
make install
```

This installs:
- `pypdf` - PDF metadata extraction
- `pdfplumber` - PDF text extraction
- `bibtexparser` - BibTeX parsing
- `pandas` - Data processing
- `requests` - HTTP requests

### 3. Optional: R for Analysis

```bash
brew install r
```

Then in R console:
```r
install.packages(c("tidyverse", "knitr", "xtable"))
```

---

## Project Structure

```
paper_r/
├── doc/                          # PDF papers (7 papers currently)
├── manuscript/                   # LaTeX manuscript
│   ├── main.tex                 # Main document
│   ├── refs.bib                 # Bibliography (manual entries)
│   ├── sections/                # Section files
│   │   ├── 01_introduction.tex
│   │   ├── 02_generative_models.tex
│   │   ├── 03_scarcity_mitigation.tex
│   │   ├── 04_modality_applications.tex
│   │   ├── 05_limitations.tex
│   │   └── 06_conclusion.tex
│   ├── figures/                 # Figures directory
│   └── tables/                  # Generated tables
├── scripts/                      # Automation scripts
│   ├── build_manuscript.sh      # LaTeX build script
│   ├── parse_refs.py           # Citation extractor
│   ├── validate_citations.py   # Citation validator
│   └── check_style.py          # Style checker
├── analysis/                     # Data analysis
│   ├── paper_metadata.csv      # Paper tracking
│   └── metrics_summary.R       # R analysis script
├── src/                         # Python utilities
├── tests/                       # Tests
├── Makefile                     # Build automation
├── CLAUDE.md                    # Project manifest
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 📖 Documentation

- **[INSTRUCTIONS.md](INSTRUCTIONS.md)** - Complete guide for editing, adding figures, tables, citations
- **[EXAMPLE_ADDITIONS.md](EXAMPLE_ADDITIONS.md)** - Practical examples of common additions
- **[CLAUDE.md](CLAUDE.md)** - Writing guidelines and project manifest

## Usage

### Build Commands

```bash
make help          # Show all available commands
make all           # Extract citations + build (full pipeline)
make build         # Compile manuscript to PDF
make quick         # Fast build (skip citation extraction)
make extract       # Extract citations from PDFs
make check         # Validate citations
make clean         # Remove build artifacts
make install       # Install Python dependencies
```

### Writing Workflow

1. **Add a new paper:**
   ```bash
   # Download PDF to doc/ folder
   cp ~/Downloads/paper.pdf doc/

   # Update metadata tracking
   # Edit analysis/paper_metadata.csv
   ```

2. **Write manuscript sections:**
   ```bash
   # Edit section files in manuscript/sections/
   vim manuscript/sections/01_introduction.tex

   # Use citations like: \cite{finetti2025data}
   ```

3. **Build and review:**
   ```bash
   # Compile to PDF
   make build

   # View output
   open manuscript/main.pdf
   ```

4. **Validate quality:**
   ```bash
   # Check citations are valid
   make check

   # Check for style issues
   python scripts/check_style.py
   ```

### Citation Management

**Manual bibliography** (recommended for accuracy):
- Edit `manuscript/refs.bib` directly
- Use keys like `finetti2025data`, `choi2017generating`

**Automatic extraction** (experimental):
```bash
make extract  # Attempts to extract from PDFs
```

**Validate citations:**
```bash
make check  # Checks all \cite{} commands are in refs.bib
```

### Paper Manuscript Structure

The review follows this outline:

1. **Introduction** - Rare disease challenges, data scarcity, evolution to generative models
2. **Generative Models** - Technical comparison of GANs, VAEs, Diffusion models
3. **Scarcity Mitigation** - How models address limited samples and class imbalance
4. **Modality Applications** - EHRs, multi-omics, medical imaging applications
5. **Limitations** - Biological variability, privacy concerns, validation challenges
6. **Conclusion** - Summary and future directions for clinical integration

---

## Writing Guidelines

### Style Requirements (from CLAUDE.md)

✅ **DO:**
- Use active voice: "Researchers applied..." not "It was applied..."
- Synthesize findings: explain *how* models address scarcity
- Back every claim with citations: `\cite{key}`
- Use academic, objective, analytical tone

❌ **AVOID:**
- "It is crucial to note"
- "Delving into"
- "It is worth noting"
- "Furthermore", "Moreover"
- "In conclusion" (use "We conclude that..." instead)

### Citation Format

IEEE numbered citations:
```latex
Finetti et al. conducted a scoping review \cite{finetti2025data}.
Multiple works have explored this \cite{choi2017generating,zhong2024meddiffusion}.
```

---

## Troubleshooting

### LaTeX Not Found

```bash
# Check if pdflatex is available
which pdflatex

# If not found, add to PATH:
export PATH="/Library/TeX/texbin:$PATH"

# Or reinstall BasicTeX
brew reinstall --cask basictex
```

### Python Package Errors

```bash
# Reinstall dependencies
make install

# Or manually:
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
```

### Build Errors

```bash
# Clean and rebuild
make clean
make build

# Check LaTeX logs
cat manuscript/main.log
```

### Citation Errors

```bash
# Validate citations first
make check

# Common issues:
# - Missing entry in refs.bib
# - Typo in citation key
# - Unclosed \cite{} command
```

---

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Quality Checks

```bash
# Style checker (prohibited phrases, passive voice)
python scripts/check_style.py

# Citation validator
python scripts/validate_citations.py
```

### Adding New Scripts

Place Python scripts in `scripts/` directory and make them executable:
```bash
chmod +x scripts/new_script.py
```

---

## Paper Metadata Tracking

Track papers in `analysis/paper_metadata.csv`:
- Filename
- Title, authors, year, venue
- DOI
- Keywords
- Status (cited, draft, read)
- Notes

Use for quantitative analysis and summary tables.

---

## Contributing

When writing:
1. Follow style guidelines in CLAUDE.md
2. Run `make check` before committing
3. Run `python scripts/check_style.py` to catch style issues
4. Ensure all sections compile without errors

---

## References

- **7 Core Papers** in `doc/` folder (see `manuscript/refs.bib` for full citations)
- **IEEE Citation Style**: [IEEEtran documentation](http://mirrors.ctan.org/macros/latex/contrib/IEEEtran/IEEEtran_HOWTO.pdf)

---

## License

Academic use only. Check with paper authors for redistribution rights.
