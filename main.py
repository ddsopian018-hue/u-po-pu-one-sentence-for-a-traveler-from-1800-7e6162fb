"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800,
built only from things they already know: a road, a library, a letter,
ink. The picture: any house on the road can open the great library, and
a letter crosses the world faster than ink dries -- and comes back
answered just as fast.
"""

import os

SENTENCE = (
    "Picture a road where any house can open the great library, and a "
    "letter written in London is read in Canton, and answered, before "
    "its ink has dried."
)


def main():
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError(
            f"entry is {len(SENTENCE)} characters, must be 1-200"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
