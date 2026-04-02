# Examples: Adding Content to Your Manuscript

This file shows practical examples of common additions to your literature review.

---

## Example 1: Adding a Paragraph with Citations

**File**: `manuscript/sections/03_scarcity_mitigation.tex`

**Add this after an existing paragraph:**

```latex
Transfer learning represents an alternative approach to addressing data scarcity
that complements synthetic generation. Researchers pretrain models on large 
datasets from related tasks before fine-tuning on small rare disease cohorts 
\cite{smith2024transfer,jones2023learning}. This technique has achieved 
diagnostic accuracies exceeding 90\% with fewer than 100 training samples, 
demonstrating that domain knowledge transfer can partially compensate for 
limited disease-specific data.
```

**Then add citations to refs.bib:**

```bibtex
@article{smith2024transfer,
  author={Smith, John and others},
  title={Transfer Learning for Rare Disease Diagnosis},
  journal={Medical AI},
  year={2024}
}
```

---

## Example 2: Adding a Figure

**Step 1**: Save your figure
```bash
cp ~/Downloads/gan_diagram.pdf manuscript/figures/gan_architecture.pdf
```

**Step 2**: Add to section file (e.g., `02_generative_models.tex`)

```latex
\subsection{Generative Adversarial Networks}

GANs employ adversarial training between two neural networks...

\begin{figure}[t]
\centering
\includegraphics[width=0.9\columnwidth]{figures/gan_architecture.pdf}
\caption{Architecture of a Generative Adversarial Network showing the generator 
network that transforms random noise into synthetic samples and the discriminator 
network that distinguishes real from generated data. The adversarial training 
process iteratively improves both networks.}
\label{fig:gan_architecture}
\end{figure}

As illustrated in Figure~\ref{fig:gan_architecture}, the generator learns to 
produce increasingly realistic samples...
```

---

## Example 3: Adding a Comparison Table

**Add to any section** (e.g., `02_generative_models.tex`):

```latex
\subsection{Comparative Analysis}

Table~\ref{tab:model_comparison} summarizes the key characteristics and 
trade-offs of different generative model architectures for rare disease 
applications.

\begin{table}[t]
\centering
\caption{Comparison of generative model architectures for biomedical data synthesis.}
\label{tab:model_comparison}
\begin{tabular}{lccc}
\hline
\textbf{Model} & \textbf{Training Time} & \textbf{Mode Collapse} & \textbf{Image Quality} \\
\hline
GAN & High & Risk & Excellent \\
VAE & Medium & None & Good \\
Diffusion & Very High & None & Excellent \\
\hline
\end{tabular}
\end{table}

The comparison reveals that model selection depends critically on available
computational resources and specific application requirements.
```

---

## Example 4: Adding a Mathematical Equation

**Add to Section 2** (technical foundations):

```latex
The GAN training objective formulates a minimax game expressed as:

\begin{equation}
\min_G \max_D V(D,G) = \mathbb{E}_{x \sim p_{data}(x)}[\log D(x)] + 
\mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\label{eq:gan_objective}
\end{equation}

where $G$ represents the generator, $D$ the discriminator, $x$ real data 
samples, and $z$ random noise vectors. As shown in Equation~\ref{eq:gan_objective}, 
the discriminator maximizes its ability to distinguish real from synthetic samples 
while the generator minimizes this discrimination.
```

---

## Example 5: Adding a New Subsection with Multiple Citations

**Add to Section 4** (modality applications):

```latex
\subsection{Tabular Clinical Data}

Beyond imaging and genomic applications, generative models have been applied 
to structured clinical databases containing laboratory results, vital signs, 
and administrative records. These tabular datasets present unique challenges 
due to mixed data types (continuous measurements, categorical variables, 
ordinal scales) and complex inter-feature dependencies \cite{xu2019modeling,
park2018data}.

CTGAN and TVAE architectures specifically address tabular data generation 
through mode-specific normalization that handles diverse data distributions 
\cite{xu2019modeling}. For rare disease applications with imbalanced class 
distributions, conditional generation enables targeted synthesis of 
underrepresented patient subgroups. Park et al. demonstrated threefold 
expansion of acute lymphoblastic leukemia patient records while maintaining 
the statistical properties of rare genetic markers \cite{park2018data}.

Privacy preservation remains particularly critical for tabular clinical data 
where demographic variables and diagnosis codes can facilitate patient 
reidentification. Differential privacy mechanisms provide formal guarantees 
but introduce utility trade-offs that require careful calibration for each 
specific application context.
```

---

## Example 6: Adding Bullet Points

**Add to Section 5** (limitations):

```latex
Several critical challenges must be addressed before widespread clinical adoption:

\begin{itemize}
\item \textbf{Validation frameworks}: Standardized protocols for assessing 
synthetic data quality remain absent, limiting reproducibility and comparison 
across studies.

\item \textbf{Regulatory pathways}: FDA and EMA guidelines for synthetic 
data-trained diagnostic tools are still under development, creating uncertainty 
for commercial deployment.

\item \textbf{Computational accessibility}: High training costs restrict access 
to smaller research institutions and patient advocacy organizations.

\item \textbf{Clinical interpretability}: Black-box models provide limited 
mechanistic insights that clinicians require for diagnostic confidence.
\end{itemize}

Addressing these challenges requires coordinated efforts across technical, 
regulatory, and clinical stakeholder communities.
```

---

## Example 7: Adding a Case Study Box (Advanced)

**Add to Section 3** (scarcity mitigation):

```latex
\subsubsection{Case Study: Synthetic Data for Duchenne Muscular Dystrophy}

Duchenne muscular dystrophy (DMD) affects approximately 1 in 5,000 male births,
resulting in limited patient cohorts for machine learning model training. 
Martinez et al. applied StyleGAN2 to generate synthetic muscle biopsy 
histopathology images from an initial dataset of only 87 DMD patient samples 
\cite{martinez2023synthetic}.

The synthetic augmentation expanded the training set to over 2,000 images, 
enabling a ResNet-50 classifier to achieve 91\% diagnostic accuracy compared 
to 76\% when trained on real data alone. Expert pathologist review confirmed 
that 94\% of synthetic samples exhibited realistic tissue architecture and 
dystrophic changes characteristic of DMD. This case demonstrates that 
generative models can provide clinically meaningful benefits even for 
ultra-rare genetic conditions with extremely limited training data.
```

---

## Example 8: Citing Multiple Papers Together

**Good citation practices:**

```latex
% Multiple papers supporting the same point
Recent studies have consistently demonstrated performance improvements through
synthetic augmentation \cite{smith2024,jones2023,wilson2024}.

% Sequential citations for different points
GANs dominate medical imaging applications \cite{fridadar2018gan}, while 
diffusion models show promise for sequential EHR data \cite{zhong2024meddiffusion}, 
and knowledge-guided approaches enable few-shot learning \cite{alsentzer2025few}.

% Contrasting findings
While Frid-Adar et al. reported 7.1 percentage point improvements 
\cite{fridadar2018gan}, other studies found more modest gains of 2-3 percentage 
points \cite{other2024}, suggesting that augmentation effectiveness varies 
substantially across disease types and dataset characteristics.
```

---

## Example 9: Adding a Future Directions Subsection

**Add to Section 6** (conclusion):

```latex
\subsection{Emerging Technologies}

Several nascent technologies promise to address current limitations in 
generative modeling for rare diseases:

\textbf{Foundation models and transfer learning}: Large-scale pretraining 
on diverse medical datasets followed by few-shot adaptation to specific rare 
diseases could reduce data requirements by orders of magnitude. Early results 
suggest that foundation models trained on millions of common disease cases 
can transfer effectively to rare conditions with fewer than 100 examples.

\textbf{Causal generative models}: Incorporating causal reasoning mechanisms 
could ensure that synthetic data respects known biological pathways and 
disease mechanisms rather than purely statistical associations. This would 
address biological plausibility concerns while enabling counterfactual 
reasoning about treatment effects.

\textbf{Multi-modal synthesis}: Jointly generating consistent data across 
imaging, genomic, and clinical modalities would capture the correlations 
present in real patients while expanding training data holistically rather 
than modality-by-modality.
```

---

## Quick Checklist Before Adding Content

✅ **Citations**
- [ ] All new papers added to `refs.bib`
- [ ] Citation keys match between text and bibliography
- [ ] Run `make check` to validate

✅ **Figures**
- [ ] Files placed in `manuscript/figures/`
- [ ] Descriptive filenames (not `figure1.png`)
- [ ] High resolution (300 DPI minimum)
- [ ] Captions explain what is shown
- [ ] Referenced in text with `Figure~\ref{}`

✅ **Tables**
- [ ] Clear column headers
- [ ] Units specified where applicable
- [ ] Caption describes content
- [ ] Referenced in text with `Table~\ref{}`

✅ **Style**
- [ ] Active voice dominant
- [ ] No LLM slop phrases
- [ ] Every claim cited
- [ ] Consistent terminology

✅ **Build**
- [ ] `make build` completes without errors
- [ ] PDF displays correctly
- [ ] All references resolve

---

## Build After Each Addition

```bash
# After adding content:
make build

# Check for errors:
cat manuscript/main.log | grep -i error

# Validate citations:
make check

# Check style:
python scripts/check_style.py

# View result:
open manuscript/main.pdf
```

---

These examples cover the most common additions you'll make to your manuscript.
For more details, see `INSTRUCTIONS.md`.
