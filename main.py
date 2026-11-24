#!/usr/bin/env python3
"""Entry generator for the make.fun bounty "Dad Joke Showdown".

Writes the one dad joke to /output/entry.txt (creating /output if
needed). Standard library only.
"""

import os

ENTRY = (
    "I tried fixing the Wi-Fi with a ladder \u2014 turns out the router "
    "just needed a better outlook on life."
)

# Competition gate: /output/entry.txt must be 1 to 200 characters.
MAX_CHARS = 200


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
