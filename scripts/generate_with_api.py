#!/usr/bin/env python3
"""
EXPERIMENTAL: Use Claude API to help generate literature review content.

WARNING: This is NOT recommended for final academic papers. Use only for:
- Initial drafts
- Brainstorming
- Understanding paper relationships

Always review, edit, and verify all API-generated content.
"""

import os
from anthropic import Anthropic

# This would require:
# pip install anthropic
# export ANTHROPIC_API_KEY="your-key-here"


def generate_section(section_name, papers_context, requirements):
    """
    Generate a section using Claude API.

    WARNING: Always review and edit the output. Do not use verbatim.
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    prompt = f"""You are helping write an academic literature review on
"Generative Models for Rare Disease Biomedical Data Synthesis".

Section: {section_name}

Papers available:
{papers_context}

Requirements:
- IEEE citation format
- Academic, objective tone
- Active voice
- Synthesize, don't just summarize
- Avoid: "It is crucial to note", "Delving into", "Furthermore"

{requirements}

Write the LaTeX section content (without \\section{{}} command, just content).
"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text


def main():
    """Example usage."""
    print("This script requires ANTHROPIC_API_KEY environment variable.")
    print("See: https://docs.anthropic.com/en/api/getting-started")
    print()
    print("Recommended: Work with Claude interactively instead of using API.")


if __name__ == "__main__":
    main()
