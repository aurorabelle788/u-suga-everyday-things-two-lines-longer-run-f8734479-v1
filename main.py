#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Stdlib only, deterministic, no network, reads nothing outside this repo.
"""

import os

ENTRY = (
    "A traffic jam is a school hallway at the final bell, when a hundred kids "
    "all try to squeeze through one door at once and everyone ends up shuffling "
    "slower than walking alone.\n"
    "The hallway shows how cars in one narrow road slow each other down, but it "
    "leaves out that cars can't slip sideways through gaps the way kids can, and "
    "that no bell ends a jam \u2014 it only clears when the road opens up.\n"
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
