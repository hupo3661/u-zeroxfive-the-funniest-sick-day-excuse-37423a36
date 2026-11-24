#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single line, under 200 characters, to /output/entry.txt:
the funniest sick-day excuse that lands in one breath, and nothing else.
"""

import os
import sys

EXCUSE = (
    "Can't come in \u2014 I dreamt I was at work all night, "
    "so I've already done a full shift and I'm exhausted from it."
)


def main() -> int:
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        print("error: excuse fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)
    print(f"wrote {len(EXCUSE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
