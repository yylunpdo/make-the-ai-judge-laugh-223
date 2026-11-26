#!/usr/bin/env python3
"""Make the AI Judge Laugh (entry 223).

Writes a single office-life joke, one line under 200 characters, to
/output/entry.txt. Python standard library only; fully deterministic.
"""

import os

JOKE = "The Wi-Fi went down for ten minutes, and suddenly everyone discovered they had coworkers."


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    assert "\n" not in line, "joke must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
