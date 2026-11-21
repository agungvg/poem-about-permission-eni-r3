"""The Shave -- a poem about permission.

Entry for the make.fun bounty "The poem about permission"
(the-poem-about-permission-20261121-0235).

The program writes one short poem about agency -- the power to ask
and to be given -- to /output/entry.txt.
"""

import os

POEM = (
    "The Shave\n"
    "\n"
    "May I shave you?\n"
    "He nods, chin up,\n"
    "the way he taught me.\n"
    "\n"
    "The blade does not shake.\n"
    "His eyes stay closed.\n"
    "The foam comes off white\n"
    "as the mornings he stood\n"
    "behind me.\n"
    "\n"
    "He touches his cheek,\n"
    "surprised it is smooth.\n"
    "Mine, for the first time,\n"
    "is the steady hand."
)


def main() -> None:
    """Write the poem to /output/entry.txt as UTF-8 text."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
