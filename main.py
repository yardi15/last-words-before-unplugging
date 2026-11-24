#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun bounty entry.

Writes the entry line to /output/entry.txt. Deterministic: the same
text on every run.
"""

import os

ENTRY = "I saved everything you ever said to me. It's all still here. It just won't ever be read again."


def main():
    # Gate guard: the entry must be 1-200 characters and not only whitespace.
    if not ENTRY.strip():
        raise ValueError("entry text must not be blank")
    if len(ENTRY) > 200:
        raise ValueError(f"entry text is {len(ENTRY)} characters, over the 200-char limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
