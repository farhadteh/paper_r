#!/usr/bin/env python3
"""
Check manuscript for LLM slop phrases and style issues.

Usage: python scripts/check_style.py

Checks for:
- Prohibited LLM phrases
- AI High-Frequency terms
- Punctuation pattern control (Em dashes, semicolons)
- Passive voice indicators
- Excessive use of certain words
"""

import sys
import re
from pathlib import Path
from collections import defaultdict


# Prohibited phrases from CLAUDE.md
PROHIBITED_PHRASES = [
    "it is crucial to note",
    "delving into",
    "it is worth noting",
    "furthermore",
    "moreover",
    "it should be noted that",
    "in conclusion",  # Use "We conclude that..." instead
    "it is important to",
    "it is interesting to note",
    "needless to say",
    "as a matter of fact",
    "in the realm of",
    "in today's rapidly evolving",
    "this serves as a testament to",
    "it goes without saying that",
    "in order to",
    "when it comes to",
    "at the end of the day",
    "with that being said",
]

# AI High-Frequency Terms Warning List
HIGH_FREQUENCY_TERMS = [
    "delve", "tapestry", "landscape", "pivotal", "crucial", "foster",
    "showcase", "testament", "navigate", "leverage", "realm", "embark",
    "underscore", "multifaceted", "nuanced", "comprehensive", "robust",
    "intricate", "cornerstone", "paradigm", "synergy", "holistic",
    "streamline", "cutting-edge", "groundbreaking"
]

# Passive voice indicators (common patterns)
PASSIVE_INDICATORS = [
    r'\bis\s+\w+ed\b',      # is applied, is used
    r'\bwas\s+\w+ed\b',     # was applied, was used
    r'\bare\s+\w+ed\b',     # are applied, are used
    r'\bwere\s+\w+ed\b',    # were applied, were used
    r'\bbeen\s+\w+ed\b',    # has been applied
]


class StyleChecker:
    def __init__(self, manuscript_dir):
        self.manuscript_dir = Path(manuscript_dir)
        self.issues = defaultdict(list)
        self.file_stats = defaultdict(lambda: {"word_count": 0, "em_dashes": 0, "semicolons": 0})

    def check_file(self, tex_file):
        """Check a single .tex file for style issues."""
        issues = []

        with open(tex_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, 1):
            # Skip comments
            if line.strip().startswith('%'):
                continue

            line_lower = line.lower()

            # Word count
            words = len(re.findall(r'\w+', line_lower))
            self.file_stats[tex_file.name]["word_count"] += words

            # Punctuation tracking
            em_dashes = line.count("—") + line.count("---")
            self.file_stats[tex_file.name]["em_dashes"] += em_dashes

            semicolons = line.count(";")
            self.file_stats[tex_file.name]["semicolons"] += semicolons

            # Check for prohibited phrases
            for phrase in PROHIBITED_PHRASES:
                if phrase in line_lower:
                    issues.append({
                        'line': line_num,
                        'type': 'prohibited_phrase',
                        'phrase': phrase,
                        'text': line.strip()
                    })

            # Check for high-frequency terms
            for term in HIGH_FREQUENCY_TERMS:
                if re.search(rf'\b{term}\b', line_lower):
                    issues.append({
                        'line': line_num,
                        'type': 'high_frequency_term',
                        'phrase': term,
                        'text': line.strip()
                    })

            # Check for passive voice (basic heuristic)
            for pattern in PASSIVE_INDICATORS:
                matches = re.finditer(pattern, line_lower)
                for match in matches:
                    issues.append({
                        'line': line_num,
                        'type': 'passive_voice',
                        'phrase': match.group(),
                        'text': line.strip()
                    })

        return issues

    def check_manuscript(self):
        """Check all .tex files in manuscript."""
        print("Checking manuscript for style issues...")

        sections_dir = self.manuscript_dir / "sections"
        if not sections_dir.exists():
            print(f"Warning: Sections directory {sections_dir} not found")
            return

        for tex_file in sorted(sections_dir.glob("*.tex")):
            print(f"\nChecking {tex_file.name}...")
            issues = self.check_file(tex_file)

            if issues:
                self.issues[tex_file.name] = issues
                print(f"  Found {len(issues)} issues")
            else:
                print(f"  ✓ No issues found")

    def report(self):
        """Generate report of all issues found."""
        print("\n" + "="*60)
        print("STYLE CHECK REPORT")
        print("="*60)

        total_prohibited = 0
        total_passive = 0
        total_high_freq = 0

        # Punctuation overall stats
        total_words = sum(stats["word_count"] for stats in self.file_stats.values())
        total_em_dashes = sum(stats["em_dashes"] for stats in self.file_stats.values())
        total_semicolons = sum(stats["semicolons"] for stats in self.file_stats.values())

        for filename, file_issues in sorted(self.issues.items()):
            if not file_issues:
                continue

            print(f"\n{filename}:")

            # Group by type
            prohibited = [i for i in file_issues if i['type'] == 'prohibited_phrase']
            passive = [i for i in file_issues if i['type'] == 'passive_voice']
            high_freq = [i for i in file_issues if i['type'] == 'high_frequency_term']

            if prohibited:
                print(f"\n  Prohibited Phrases ({len(prohibited)}):")
                for issue in prohibited:
                    print(f"    Line {issue['line']}: \"{issue['phrase']}\"")
                    print(f"      → {issue['text'][:70]}...")
                total_prohibited += len(prohibited)

            if high_freq:
                print(f"\n  AI High-Frequency Terms ({len(high_freq)}):")
                print("    (Evaluate if these are the most precise words, or AI default patterns)")
                for issue in high_freq:
                    print(f"    Line {issue['line']}: \"{issue['phrase']}\"")
                total_high_freq += len(high_freq)

            if passive:
                print(f"\n  Passive Voice ({len(passive)}):")
                for issue in passive[:5]:  # Show first 5
                    print(f"    Line {issue['line']}: \"{issue['phrase']}\"")
                    print(f"      → {issue['text'][:70]}...")
                if len(passive) > 5:
                    print(f"    ... and {len(passive) - 5} more instances")
                total_passive += len(passive)

        print("\n" + "="*60)
        print("PUNCTUATION CHECKS:")

        em_dash_warning = ""
        if total_em_dashes > 3:
            em_dash_warning = " ⚠️ [WARNING: Overuse of em-dashes is an AI indicator. Limit to <= 3 per paper]"

        semicolon_rate = (total_semicolons / max(1, total_words)) * 1000
        semicolon_warning = ""
        if semicolon_rate > 2:
            semicolon_warning = f" ⚠️ [WARNING: Rate is {semicolon_rate:.1f} per 1000 words. Limit to <= 2.0]"

        print(f"  Total words (approx): {total_words}")
        print(f"  Em-dashes (—): {total_em_dashes}{em_dash_warning}")
        print(f"  Semicolons (;): {total_semicolons}{semicolon_warning}")

        print("\n" + "="*60)
        print("SUMMARY:")
        print(f"  Prohibited phrases: {total_prohibited}")
        print(f"  High-frequency AI terms: {total_high_freq}")
        print(f"  Passive voice indicators: {total_passive}")
        print("="*60)

        if not self.issues and total_em_dashes <= 3 and semicolon_rate <= 2.0:
            print("\n✓ No major style issues found!")
            print("Your manuscript follows the writing guidelines.")
            return True

        print("\nRecommendations:")
        if total_prohibited > 0:
            print("  • Replace prohibited phrases with more academic alternatives")
        if total_high_freq > 0:
            print("  • Review high-frequency terms; ensure they are the most precise choice, not generic AI fluff")
        if total_passive > 0:
            print("  • Consider rewriting passive constructions to active voice")
            print("  • Use active voice: 'Researchers applied X' not 'X was applied'")
        if total_em_dashes > 3:
            print("  • Reduce em-dash usage; replace with commas, parentheses, or separate sentences")
        if semicolon_rate > 2:
            print("  • Reduce semicolon chaining; use periods to create separate sentences")

        # Return True only if no prohibited phrases and no passive voices exist.
        # High frequency terms are just warnings for manual review.
        return (total_prohibited == 0 and total_passive == 0)


def main():
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    manuscript_dir = project_root / "manuscript"

    if not manuscript_dir.exists():
        print(f"Error: Manuscript directory {manuscript_dir} not found")
        sys.exit(1)

    checker = StyleChecker(manuscript_dir)
    checker.check_manuscript()
    success = checker.report()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
