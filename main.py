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


def validate(text: str) -> str:
    """Check the excuse against the brief; return it unchanged if valid.

    The brief requires a single line of 1-200 characters that is not
    blank. Raises ValueError naming the first failed rule.
    """
    if not text.strip():
        raise ValueError("excuse must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"excuse must be 1-200 characters, got {len(text)}"
        )
    return text


def main() -> int:
    try:
        excuse = validate(EXCUSE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse)
    print(excuse)
    print(f"wrote {len(excuse)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
