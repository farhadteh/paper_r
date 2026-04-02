#!/bin/bash
set -e

# Add TeX to PATH
export PATH="/Library/TeX/texbin:$PATH"

echo "Building manuscript..."
cd "$(dirname "$0")/../manuscript"

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "Error: pdflatex not found. Please install BasicTeX or MacTeX."
    echo "Run: brew install --cask basictex"
    echo "Then add to PATH: export PATH=\"/Library/TeX/texbin:\$PATH\""
    exit 1
fi

# Run LaTeX compilation sequence
echo "Running pdflatex (pass 1)..."
pdflatex -interaction=nonstopmode main.tex

echo "Running bibtex..."
bibtex main || echo "Warning: bibtex had issues (may be normal if no citations yet)"

echo "Running pdflatex (pass 2)..."
pdflatex -interaction=nonstopmode main.tex

echo "Running pdflatex (pass 3)..."
pdflatex -interaction=nonstopmode main.tex

# Cleanup auxiliary files
echo "Cleaning up auxiliary files..."
rm -f *.aux *.log *.bbl *.blg *.out *.toc *.synctex.gz

echo "✓ Build complete: manuscript/main.pdf"
