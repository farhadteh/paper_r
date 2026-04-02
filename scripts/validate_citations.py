#!/usr/bin/env python3
"""
Validate citations in LaTeX manuscript against refs.bib.

Usage: python scripts/validate_citations.py

Checks:
- All \\cite{} commands reference entries in refs.bib
- Reports missing citations
- Reports unused bibliography entries
"""

import sys
import re
from pathlib import Path


class CitationValidator:
    def __init__(self, manuscript_dir, bib_file):
        self.manuscript_dir = Path(manuscript_dir)
        self.bib_file = Path(bib_file)
        self.cited_keys = set()
        self.bib_keys = set()

    def extract_citations_from_tex(self, tex_file):
        """Extract all \\cite{} commands from a .tex file."""
        citations = set()

        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()

            # Match \cite{key}, \cite{key1,key2}, etc.
            cite_pattern = r'\\cite\{([^}]+)\}'
            matches = re.findall(cite_pattern, content)

            for match in matches:
                # Handle multiple keys in one cite command
                keys = [k.strip() for k in match.split(',')]
                citations.update(keys)

        return citations

    def extract_keys_from_bib(self):
        """Extract all citation keys from refs.bib."""
        keys = set()

        if not self.bib_file.exists():
            print(f"Warning: Bibliography file {self.bib_file} not found")
            return keys

        with open(self.bib_file, 'r', encoding='utf-8') as f:
            content = f.read()

            # Match @article{key, @inproceedings{key, etc.
            key_pattern = r'@\w+\{([^,\s]+),'
            matches = re.findall(key_pattern, content)
            keys.update(matches)

        return keys

    def scan_manuscript(self):
        """Scan all .tex files in manuscript directory."""
        print("Scanning manuscript for citations...")

        # Check main.tex
        main_tex = self.manuscript_dir / "main.tex"
        if main_tex.exists():
            cites = self.extract_citations_from_tex(main_tex)
            self.cited_keys.update(cites)
            print(f"  main.tex: {len(cites)} citations")

        # Check section files
        sections_dir = self.manuscript_dir / "sections"
        if sections_dir.exists():
            for tex_file in sorted(sections_dir.glob("*.tex")):
                cites = self.extract_citations_from_tex(tex_file)
                self.cited_keys.update(cites)
                print(f"  {tex_file.name}: {len(cites)} citations")

        print(f"\nTotal unique citations found: {len(self.cited_keys)}")

    def validate(self):
        """Validate citations against bibliography."""
        print("\nValidating citations against refs.bib...")

        self.bib_keys = self.extract_keys_from_bib()
        print(f"Bibliography entries: {len(self.bib_keys)}")

        # Find missing citations (cited but not in bib)
        missing = self.cited_keys - self.bib_keys

        # Find unused entries (in bib but not cited)
        unused = self.bib_keys - self.cited_keys

        # Report results
        print("\n" + "="*60)
        print("VALIDATION RESULTS")
        print("="*60)

        if not missing and not unused:
            print("✓ All citations are valid!")
            print("✓ All bibliography entries are used!")
            return True

        success = True

        if missing:
            print(f"\n✗ MISSING CITATIONS ({len(missing)}):")
            print("  The following keys are cited but not in refs.bib:")
            for key in sorted(missing):
                print(f"    - {key}")
            success = False

        if unused:
            print(f"\n⚠ UNUSED ENTRIES ({len(unused)}):")
            print("  The following keys are in refs.bib but not cited:")
            for key in sorted(unused):
                print(f"    - {key}")
            print("  (This is not an error, but you may want to remove them)")

        return success


def main():
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    manuscript_dir = project_root / "manuscript"
    bib_file = manuscript_dir / "refs.bib"

    if not manuscript_dir.exists():
        print(f"Error: Manuscript directory {manuscript_dir} not found")
        sys.exit(1)

    validator = CitationValidator(manuscript_dir, bib_file)
    validator.scan_manuscript()
    success = validator.validate()

    print("\n" + "="*60)
    if success:
        print("Citation validation passed!")
    else:
        print("Citation validation found issues.")
        print("Please fix missing citations before building.")
    print("="*60)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
