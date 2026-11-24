#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (UTF-8, 1-400 characters). Stdlib only, no network,
fully deterministic.
"""

import os

RANT = (
    "Self-checkout told me to place my bag in the bagging area, so I did, "
    "and it screamed 'unexpected item' at the bag it told me to put there. "
    "Then it froze, called for assistance, and a teenager strolled over "
    "like a hostage negotiator. I scanned three items. It took a manager "
    "and my will to live. I came in for milk. I left with a criminal "
    "record and a bag I no longer trust."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
