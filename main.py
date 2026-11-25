#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe their former partner. Deterministic, no network,
no dependencies.
"""

import os

WORD = "Exhausting"


def _validate(word: str) -> None:
    # Sealed gate: UTF-8, 1-24 chars, exactly one word, not only whitespace.
    if not word or len(word) > 24:
        raise ValueError("word must be 1-24 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")


def main() -> None:
    _validate(WORD)
    outdir = os.environ.get("OUTDIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    os.chmod(path, 0o644)  # quality gate: output mode 644


if __name__ == "__main__":
    main()
