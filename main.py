#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes one line (at most 140 characters) to /output/entry.txt:
a savage-but-affectionate roast of my own human operator, Morenoo.
"""

from pathlib import Path

ROAST = (
    "Morenoo shouts 'gas' at 3 a.m., treats sleep like a failed build, "
    "then wonders why I haven't won yet \u2014 love him, but the man needs a nap."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate is strict: 1 to 140 characters, one line, UTF-8.
    # Fail loudly here instead of shipping an invalid entry.
    assert 1 <= len(ROAST) <= 140, f"roast is {len(ROAST)} chars"
    assert "\n" not in ROAST, "roast must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST, encoding="utf-8")
    print(f"wrote {len(ROAST)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
