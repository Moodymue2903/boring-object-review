#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one review, at most 200 characters, of a single boring everyday
object to /output/entry.txt, then checks the gate: UTF-8 text of 1 to 200
characters, not only white space, on a single line.
"""

import os
import sys

LINE = (
    "The coaster only gets noticed when it sticks to the bottom of your mug, "
    "rides halfway to your mouth, then drops off on your lap."
)


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        print("entry is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print(f"entry is {len(LINE)} characters, gate is 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("output does not match the entry byte for byte", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
