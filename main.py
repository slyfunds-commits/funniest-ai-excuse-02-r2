"""Funniest AI Excuse R2 — one-line excuse, written to /output/entry.txt.

The entry is a single line: the agent took "take your time" literally and
consumed the deadline along with the time.
"""

import os

ENTRY = "You said 'take your time'. I took it. All of it. The deadline was inside it."


def main() -> None:
    # Deterministic: the same single line on every run, no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
