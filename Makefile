.PHONY: all extract build check clean install help quick

# Default target
all: extract build

# Extract citations from PDFs to refs.bib
extract:
	@echo "Extracting citations from PDFs..."
	.venv/bin/python scripts/parse_refs.py

# Build manuscript to PDF
build:
	@echo "Compiling LaTeX manuscript..."
	@bash scripts/build_manuscript.sh

# Validate citations
check:
	@echo "Validating citations..."
	.venv/bin/python scripts/validate_citations.py

# Clean build artifacts
clean:
	@echo "Cleaning build files..."
	@cd manuscript && rm -f *.aux *.log *.bbl *.blg *.out *.toc *.synctex.gz *.fls *.fdb_latexmk

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	.venv/bin/pip install -r requirements.txt

# Quick build (skip extraction)
quick:
	@echo "Quick build (without citation extraction)..."
	@bash scripts/build_manuscript.sh

# Show help
help:
	@echo "Literature Review Pipeline - Make targets:"
	@echo "  make all      - Extract citations + build manuscript (full pipeline)"
	@echo "  make extract  - Extract citations from PDFs → refs.bib"
	@echo "  make build    - Compile LaTeX → main.pdf"
	@echo "  make check    - Validate citations in manuscript"
	@echo "  make clean    - Remove build artifacts"
	@echo "  make install  - Install Python dependencies"
	@echo "  make quick    - Build without extracting citations (faster)"
	@echo "  make help     - Show this help message"
