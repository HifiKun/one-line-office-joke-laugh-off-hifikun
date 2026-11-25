#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off.

Writes a single original one-line joke about office life to
/output/entry.txt.
"""

import os

# The joke: one line about office life. The punchline lands on the gap
# between the team-building poster and who actually carries the work.
ENTRY = (
    "Our team-building exercise was carrying the whole project while "
    "management posed for the photo."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
