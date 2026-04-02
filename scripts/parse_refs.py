#!/usr/bin/env python3
"""
Extract citations from PDF papers and generate BibTeX bibliography.

Usage: python scripts/parse_refs.py
Output: manuscript/refs.bib

Note: This script provides basic PDF metadata extraction. For encrypted or
image-only PDFs, manual entries in refs.bib may be required.
"""

import sys
from pathlib import Path
import re

try:
    import pypdf
    import pdfplumber
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip install pypdf pdfplumber")
    sys.exit(1)


class CitationExtractor:
    def __init__(self, doc_dir, output_bib):
        self.doc_dir = Path(doc_dir)
        self.output_bib = Path(output_bib)
        self.entries = []

    def extract_metadata(self, pdf_path):
        """Extract title, authors, year from PDF metadata and text."""
        metadata = {
            'filename': pdf_path.stem,
            'title': None,
            'author': None,
            'year': None,
        }

        try:
            # Try pypdf for metadata
            with open(pdf_path, 'rb') as f:
                reader = pypdf.PdfReader(f)
                info = reader.metadata

                if info:
                    metadata['title'] = info.get('/Title', '').strip()
                    metadata['author'] = info.get('/Author', '').strip()

                    # Try to extract year from creation date
                    creation_date = info.get('/CreationDate', '')
                    year_match = re.search(r'(\d{4})', str(creation_date))
                    if year_match:
                        metadata['year'] = year_match.group(1)

            # If metadata is insufficient, try pdfplumber for text extraction
            if not metadata['title'] or not metadata['author']:
                with pdfplumber.open(pdf_path) as pdf:
                    if len(pdf.pages) > 0:
                        first_page = pdf.pages[0].extract_text()
                        if first_page:
                            # Heuristic: title is often in first few lines
                            lines = first_page.split('\n')[:10]
                            # This is a simple heuristic - may need refinement
                            if not metadata['title'] and lines:
                                metadata['title'] = lines[0].strip()

                            # Look for year in first page
                            if not metadata['year']:
                                year_match = re.search(r'\b(19|20)\d{2}\b', first_page)
                                if year_match:
                                    metadata['year'] = year_match.group(0)

        except Exception as e:
            print(f"Warning: Could not extract metadata from {pdf_path.name}: {e}")

        return metadata

    def generate_bibtex_key(self, metadata):
        """Generate a BibTeX citation key from metadata."""
        # Default key format: author_year or filename
        key = metadata['filename'].lower().replace(' ', '_').replace('-', '_')
        return key

    def generate_bibtex_entry(self, metadata):
        """Convert metadata to BibTeX format."""
        key = self.generate_bibtex_key(metadata)

        # Default to @article, could be refined based on content
        entry = f"@article{{{key},\n"

        if metadata['author']:
            entry += f"  author={{{metadata['author']}}},\n"
        else:
            entry += f"  author={{Unknown}},\n"

        if metadata['title']:
            entry += f"  title={{{metadata['title']}}},\n"
        else:
            entry += f"  title={{Extracted from {metadata['filename']}}},\n"

        if metadata['year']:
            entry += f"  year={{{metadata['year']}}},\n"

        entry += f"  note={{Filename: {metadata['filename']}}}\n"
        entry += "}\n"

        return entry

    def process_all_pdfs(self):
        """Scan doc/ directory and extract citations."""
        print(f"Scanning {self.doc_dir} for PDF files...")

        pdf_files = list(self.doc_dir.glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDF files")

        for pdf_path in pdf_files:
            print(f"Processing: {pdf_path.name}")
            try:
                metadata = self.extract_metadata(pdf_path)
                entry = self.generate_bibtex_entry(metadata)
                self.entries.append(entry)
                print(f"  ✓ Extracted: {metadata.get('title', 'No title')[:60]}")
            except Exception as e:
                print(f"  ✗ Error processing {pdf_path.name}: {e}")

        self.write_bibliography()

    def write_bibliography(self):
        """Write or update refs.bib file."""
        print(f"\nWriting bibliography to {self.output_bib}...")

        # Read existing manual entries if file exists
        existing_content = ""
        if self.output_bib.exists():
            with open(self.output_bib, 'r') as f:
                existing_content = f.read()
            print("  Note: Existing refs.bib found. Manual entries will be preserved.")

        # Write header + extracted entries
        with open(self.output_bib, 'w') as f:
            f.write("% Bibliography for Literature Review\n")
            f.write("% Generative Models for Rare Disease Biomedical Data Synthesis\n")
            f.write("% \n")
            f.write("% This file contains both manual entries and auto-extracted entries.\n")
            f.write("% Manual entries should be edited for accuracy.\n\n")

            # If there's existing content, preserve it
            if existing_content:
                f.write("% === EXISTING MANUAL ENTRIES ===\n\n")
                f.write(existing_content)
                f.write("\n\n% === AUTO-EXTRACTED ENTRIES ===\n")
                f.write("% (These may need manual refinement)\n\n")

            for entry in self.entries:
                f.write(entry)
                f.write("\n")

        print(f"✓ Bibliography written with {len(self.entries)} entries")
        print("\nNote: Auto-extracted entries may need manual refinement for accuracy.")


def main():
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    doc_dir = project_root / "doc"
    output_bib = project_root / "manuscript" / "refs.bib"

    if not doc_dir.exists():
        print(f"Error: Directory {doc_dir} not found")
        sys.exit(1)

    extractor = CitationExtractor(doc_dir, output_bib)
    extractor.process_all_pdfs()

    print("\n" + "="*60)
    print("Citation extraction complete!")
    print("Please review and refine entries in manuscript/refs.bib")
    print("="*60)


if __name__ == "__main__":
    main()
