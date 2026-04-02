# Instructions: Working with Your Literature Review Manuscript

This guide explains how to add, edit, and manage content in your literature review on "Generative Models for Rare Disease Biomedical Data Synthesis."

---

## 📁 Project Structure

```
paper_r/
├── manuscript/
│   ├── main.tex                 # Main document (DO NOT edit content here)
│   ├── refs.bib                 # Bibliography (add/edit citations here)
│   ├── sections/                # Edit these files to change content
│   │   ├── 01_introduction.tex
│   │   ├── 02_generative_models.tex
│   │   ├── 03_scarcity_mitigation.tex
│   │   ├── 04_modality_applications.tex
│   │   ├── 05_limitations.tex
│   │   └── 06_conclusion.tex
│   ├── figures/                 # Put figure files here (PNG, PDF, JPG)
│   ├── tables/                  # Put generated tables here
│   └── main.pdf                 # Output PDF (regenerated on each build)
├── scripts/
│   ├── build_manuscript.sh      # Build script
│   ├── validate_citations.py   # Check citations
│   └── check_style.py          # Check writing style
├── doc/                         # Your source PDF papers
├── Makefile                     # Build automation
└── CLAUDE.md                    # Writing guidelines
```

---

## ✏️ Editing Existing Content

### Step 1: Open the Section File

Navigate to the section you want to edit:

```bash
# Example: Edit the introduction
vim manuscript/sections/01_introduction.tex
# Or use your preferred editor (VS Code, nano, etc.)
```

### Step 2: Make Your Changes

- Edit the LaTeX text directly
- Keep the `\section{Title}` and `\label{sec:name}` lines at the top
- Use `\cite{key}` for citations (see below)

### Step 3: Build and View

```bash
make build
open manuscript/main.pdf
```

---

## ➕ Adding New Content

### Adding a New Paragraph

Simply add text to any section file:

```latex
\section{Introduction}
\label{sec:intro}

Existing paragraph here.

This is my new paragraph with important information \cite{author2024}.
The text continues with more details.
```

### Adding a New Subsection

```latex
\subsection{My New Subsection}

Content for the new subsection goes here. You can add multiple paragraphs
and cite papers \cite{paper1,paper2}.

More content in this subsection.
```

### Adding a New Subsubsection (if needed)

```latex
\subsubsection{Specific Topic}

Detailed content about a specific topic.
```

---

## 📊 Adding Figures

### Step 1: Prepare Your Figure

- Save your figure file in `manuscript/figures/`
- Supported formats: PDF (best for vector graphics), PNG, JPG
- Recommended naming: `descriptive_name.pdf` or `figure1_gan_architecture.png`

```bash
cp ~/Downloads/my_figure.pdf manuscript/figures/gan_architecture.pdf
```

### Step 2: Add Figure to Your Section

```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.8\columnwidth]{figures/gan_architecture.pdf}
\caption{GAN architecture showing generator and discriminator networks. 
The generator transforms random noise into synthetic medical images while 
the discriminator learns to distinguish real from generated samples.}
\label{fig:gan_arch}
\end{figure}
```

### Step 3: Reference the Figure in Text

```latex
As shown in Figure~\ref{fig:gan_arch}, the GAN architecture consists of...
```

### Figure Position Options

- `[t]` - Top of page (recommended for IEEE format)
- `[h]` - Here (approximately where you place it)
- `[b]` - Bottom of page
- `[p]` - Separate page of floats

### Figure Width Options

- `width=0.5\columnwidth` - Half column width
- `width=0.8\columnwidth` - 80% of column width
- `width=\columnwidth` - Full column width
- `width=0.9\textwidth` - 90% of text width (for 2-column spanning)

---

## 📈 Adding Tables

### Simple Table Example

```latex
\begin{table}[t]
\centering
\caption{Performance comparison of generative models on rare disease datasets.}
\label{tab:performance}
\begin{tabular}{lcccc}
\hline
Model & Accuracy & Sensitivity & Specificity & Dataset Size \\
\hline
GAN & 85.7\% & 78.6\% & 92.4\% & 182 \\
VAE & 82.3\% & 75.2\% & 88.9\% & 182 \\
Diffusion & 87.1\% & 81.4\% & 93.8\% & 182 \\
\hline
\end{tabular}
\end{table}
```

### Reference the Table

```latex
Table~\ref{tab:performance} shows that diffusion models achieved...
```

### Table Formatting Tips

- `l` = Left-aligned column
- `c` = Center-aligned column
- `r` = Right-aligned column
- `|` = Vertical line between columns
- `\hline` = Horizontal line

### Multi-line Cells

```latex
\begin{tabular}{l p{5cm}}
Model & Description \\
\hline
GAN & Adversarial training between generator and discriminator networks \\
VAE & Probabilistic encoder-decoder with latent space regularization \\
\end{tabular}
```

---

## 📚 Adding Citations

### Step 1: Add Entry to refs.bib

Open `manuscript/refs.bib` and add a new entry:

```bibtex
@article{smith2024deep,
  author={Smith, John and Doe, Jane},
  title={Deep Learning for Rare Diseases},
  journal={Nature Medicine},
  year={2024},
  volume={30},
  number={5},
  pages={123-134},
  doi={10.1038/s41591-024-12345-6}
}
```

### Step 2: Cite in Your Text

```latex
Recent work has demonstrated promising results \cite{smith2024deep}.

Multiple studies \cite{smith2024deep,jones2023gan} have shown...
```

### Step 3: Build to Update Bibliography

```bash
make build
```

### Citation Entry Types

**Journal Article:**
```bibtex
@article{key,
  author={},
  title={},
  journal={},
  year={},
  volume={},
  number={},
  pages={}
}
```

**Conference Paper:**
```bibtex
@inproceedings{key,
  author={},
  title={},
  booktitle={},
  year={},
  pages={}
}
```

**Book:**
```bibtex
@book{key,
  author={},
  title={},
  publisher={},
  year={}
}
```

---

## 🔨 Building the Manuscript

### Quick Build (Recommended)

```bash
make build
```

This runs the full LaTeX → BibTeX → LaTeX → LaTeX cycle.

### Fast Build (During Editing)

```bash
make quick
```

Skips citation extraction, faster for iterative editing.

### View the PDF

```bash
open manuscript/main.pdf
```

### Clean Build Artifacts

```bash
make clean
```

Removes `.aux`, `.log`, `.bbl`, `.blg`, etc.

---

## ✅ Validation and Quality Checks

### Check Citations

```bash
make check
# Or directly:
.venv/bin/python scripts/validate_citations.py
```

**Output:**
- Lists all citations found in sections
- Checks if they exist in refs.bib
- Reports unused bibliography entries
- Reports missing citations

### Check Writing Style

```bash
.venv/bin/python scripts/check_style.py
```

**Checks for:**
- Prohibited LLM phrases ("It is crucial to note", "Delving into", etc.)
- Excessive passive voice
- Style issues

### All Commands

```bash
make help
```

Shows all available commands.

---

## 🎨 LaTeX Formatting Tips

### Emphasis

```latex
\emph{emphasized text}          % Italic
\textbf{bold text}              % Bold
\texttt{monospace text}         % Code/typewriter font
```

### Lists

**Bulleted List:**
```latex
\begin{itemize}
  \item First item
  \item Second item
  \item Third item
\end{itemize}
```

**Numbered List:**
```latex
\begin{enumerate}
  \item First item
  \item Second item
  \item Third item
\end{enumerate}
```

### Math Equations

**Inline Math:**
```latex
The accuracy is $\alpha = 0.85$.
```

**Display Math:**
```latex
\begin{equation}
  \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
  \label{eq:accuracy}
\end{equation}
```

**Reference Equation:**
```latex
As shown in Equation~\ref{eq:accuracy}, the accuracy is computed...
```

### Special Characters

```latex
\%       % Percent sign
\$       % Dollar sign
\&       % Ampersand
\_       % Underscore
\#       % Hash
\{       % Left brace
\}       % Right brace
```

---

## 🔗 Cross-References

### Referencing Sections

```latex
As discussed in Section~\ref{sec:methods}, the model architecture...
```

### Referencing Figures

```latex
Figure~\ref{fig:results} shows the performance comparison...
```

### Referencing Tables

```latex
The results in Table~\ref{tab:metrics} demonstrate...
```

### Referencing Equations

```latex
According to Equation~\ref{eq:loss}, the loss function...
```

**Always use `~` (non-breaking space) before `\ref` to prevent line breaks.**

---

## 📝 Writing Style Guidelines (from CLAUDE.md)

### ✅ DO:

- **Use active voice**: "Researchers applied X" not "X was applied"
- **Synthesize findings**: Explain *how* models address problems
- **Back every claim**: Use `\cite{}` for all assertions
- **Use academic tone**: Objective, analytical
- **Be specific**: Include metrics, numbers, results

### ❌ AVOID:

- "It is crucial to note"
- "Delving into"
- "It is worth noting"
- "Furthermore" (use specific transitions)
- "Moreover"
- "In conclusion" (use "We conclude that...")

### Citation Best Practices

```latex
% Good - Active voice with citation
Frid-Adar et al. achieved 85.7\% sensitivity using GAN-based 
augmentation \cite{fridadar2018gan}.

% Bad - Passive voice, vague
It has been shown that GANs can improve performance \cite{fridadar2018gan}.
```

---

## 🐛 Troubleshooting

### LaTeX Build Errors

**Error: "Undefined control sequence"**
- Check for typos in LaTeX commands
- Ensure all `{` have matching `}`
- Verify `\cite{}` keys match refs.bib

**Error: "File not found"**
- Check figure paths: `figures/myimage.pdf`
- Ensure files are in `manuscript/figures/`
- File names are case-sensitive

**Error: "Missing $ inserted"**
- Math symbols must be in math mode: `$\alpha$`
- Use `\%` instead of bare `%` for percent signs

### Citation Errors

**Error: "Citation undefined"**
```bash
# Run full build cycle
make build

# If still failing, check:
# 1. Citation key in refs.bib matches \cite{key}
# 2. No typos in citation key
# 3. BibTeX entry is properly formatted
```

**Error: "Empty bibliography"**
- Ensure you have `\cite{}` commands in your sections
- Check that `refs.bib` has entries
- Run `make build` (not `make quick`)

### Build Not Updating

```bash
# Clean and rebuild
make clean
make build
```

### PDF Won't Open

```bash
# Check for build errors
cat manuscript/main.log | grep -i error
```

---

## 📦 Adding New Sections (Advanced)

### Step 1: Create New Section File

```bash
touch manuscript/sections/07_new_section.tex
```

### Step 2: Add Content

```latex
\section{Your New Section Title}
\label{sec:newsection}

Your content here...
```

### Step 3: Include in main.tex

Edit `manuscript/main.tex` and add:

```latex
\input{sections/01_introduction}
\input{sections/02_generative_models}
% ... existing sections ...
\input{sections/07_new_section}    % Add this line
\input{sections/06_conclusion}
```

### Step 4: Build

```bash
make build
```

---

## 🔄 Workflow Summary

### Daily Editing Workflow

1. **Edit section file**
   ```bash
   vim manuscript/sections/02_generative_models.tex
   ```

2. **Quick build to preview**
   ```bash
   make quick
   open manuscript/main.pdf
   ```

3. **Check style (periodically)**
   ```bash
   .venv/bin/python scripts/check_style.py
   ```

4. **Full build before commit**
   ```bash
   make build
   ```

### Adding New Content Workflow

1. **Add citation to refs.bib**
2. **Edit section file with new content + `\cite{}`**
3. **Add figures to `manuscript/figures/`** (if needed)
4. **Build and validate**
   ```bash
   make build
   make check
   ```

### Final Review Workflow

1. **Full build**
   ```bash
   make clean
   make build
   ```

2. **Validate everything**
   ```bash
   make check
   .venv/bin/python scripts/check_style.py
   ```

3. **Review PDF**
   ```bash
   open manuscript/main.pdf
   ```

4. **Commit changes**
   ```bash
   git add manuscript/ doc/
   git commit -m "Updated literature review sections"
   ```

---

## 📞 Getting Help

### Check Logs

```bash
# LaTeX compilation log
cat manuscript/main.log

# BibTeX log
cat manuscript/main.blg

# Recent errors only
cat manuscript/main.log | grep -i error
```

### Useful Commands

```bash
# Show all make targets
make help

# Check citation keys in refs.bib
grep "@" manuscript/refs.bib

# Count words in sections (approximate)
wc -w manuscript/sections/*.tex

# Find all citations in text
grep -h "cite{" manuscript/sections/*.tex
```

### Resources

- **LaTeX Guide**: https://www.overleaf.com/learn
- **IEEE Citation Style**: http://www.michaelshell.org/tex/ieeetran/
- **Project Documentation**: See `README.md` and `CLAUDE.md`

---

## 🎯 Quick Reference Card

```bash
# Build manuscript
make build                      # Full build with citations
make quick                      # Fast build, skip citations

# Quality checks
make check                      # Validate citations
python scripts/check_style.py   # Check writing style

# View output
open manuscript/main.pdf        # Open PDF

# Clean up
make clean                      # Remove build artifacts

# Citation format in text
\cite{key}                      # Single citation
\cite{key1,key2}               # Multiple citations

# Cross-references
Section~\ref{sec:label}         # Reference section
Figure~\ref{fig:label}          # Reference figure
Table~\ref{tab:label}           # Reference table
```

---

## ✨ Tips for Success

1. **Build frequently** - Catch errors early
2. **Use meaningful labels** - `\label{sec:methods}` not `\label{s1}`
3. **Keep backups** - Commit to git regularly
4. **Check citations** - Run `make check` before finalizing
5. **Follow style guide** - See `CLAUDE.md` for writing guidelines
6. **Test figures** - Ensure they appear correctly in PDF
7. **Use version control** - Git tracks changes effectively

---

**Happy Writing!** 📝✨

For questions or issues, refer to `README.md` or check the LaTeX logs.
