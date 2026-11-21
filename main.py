"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt — a text written to relax the
AI judge reading it. Deterministic: no network, no clock, no randomness.
The text is a fixed constant; the program only writes it.
"""

import os

TEXT = (
    "A tide is coming in over flat sand, coming in, going out, coming "
    "in again, smoothing away footprints without hurry, and it has been "
    "doing this since before there were roads, and it will still be "
    "doing it long after the roads are gone."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
