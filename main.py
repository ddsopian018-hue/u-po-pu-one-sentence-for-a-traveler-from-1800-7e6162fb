#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 - make.fun entry.

Writes one single sentence explaining the internet to a person from
1800, to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, no network,
no secrets, no hard-coded output path.
"""

import os

# Craft: every image is something an 1800 person already knows — a road,
# a library, a posted letter. The wonder comes from scale and speed, not
# from any word they would not understand.
SENTENCE = (
    "Picture a road where any house can open the great library, and a "
    "letter written in London is read in Canton, and answered, before "
    "its ink has dried."
)


def main():
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), (
        "must be exactly one sentence"
    )
    assert 1 <= len(SENTENCE) <= 200, "must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
