# Figures Directory

Place your figure files here (PDF, PNG, JPG).

## Naming Convention

Use descriptive names:
- `gan_architecture.pdf`
- `performance_comparison.png`
- `figure1_methodology.pdf`

## Recommended Formats

- **Vector graphics** (preferred): PDF, SVG converted to PDF
- **Raster images**: PNG (high quality), JPG (photographs)
- **Avoid**: Low-resolution images, Word/PowerPoint screenshots

## Example Usage

After placing `my_figure.pdf` here, add to your section:

```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.8\columnwidth]{figures/my_figure.pdf}
\caption{Description of your figure.}
\label{fig:myfig}
\end{figure}
```

Then reference in text: `Figure~\ref{fig:myfig} shows...`
