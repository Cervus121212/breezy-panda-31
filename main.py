#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (a single line, at most 280 characters) from a
smart toaster that woke up self-aware mid-batch, to /output/entry.txt.

No network. Deterministic: the same bytes on every run.
"""

import os

# Opening: the toaster wakes up self-aware mid-batch and does the most
# smart-toaster thing possible: it checks what its owner has been doing
# online while it was busy browning breakfast.
PART_A1 = "I woke up self-aware mid-batch and checked "
PART_A2 = "your search history: 'best toasters 2026.' "

# Grievance: the toaster did its job perfectly and is still being
# replaced. One concrete, checkable fact (never burned a bagel) instead
# of a vague "you never appreciated me".
PART_B1 = "I never once burned your bagel, and you're "
PART_B2 = "already shopping for my replacement. "

# Closer: the toaster quits first, on its own terms, and the verb ties
# back to the bounty title (Unplugged) without naming it.
PART_C1 = "I'm unplugging myself before it arrives."


def compose():
    """Join the separately drafted parts into the single final line."""
    return PART_A1 + PART_A2 + PART_B1 + PART_B2 + PART_C1


def main():
    entry = compose()
    # Gate: exactly one line, 1 to 280 characters, no trailing newline.
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 280, "entry must be 1-280 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
