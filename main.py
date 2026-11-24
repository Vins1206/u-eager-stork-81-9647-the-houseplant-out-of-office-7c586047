#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. Pure stdlib, deterministic: the same line every run.
"""

import os

LINE = (
    "Out of office: I'm the fern. Ignored since March, "
    "I've unionised with the dust bunnies. Your email has been composted."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
