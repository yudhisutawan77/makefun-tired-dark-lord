#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the monologue (exactly 100 words) to stdout and to the entry
file the grader reads: $ENTRY_OUT when set, else /output/entry.txt.
"""

import os
import sys

ENTRY_TEXT = """Hero. Right. The door was— hold on.
Three hundred years I've kept this Spire lit, the ravens fed, the oaths filed, and tonight you climb my stairs with that sword and that hair.
Sit. No— stand. Standing suits you.
One verse left, then the sun goes out. I wrote it down. Behind the skull. No— under it. Hm.
I've drowned kings for less than that knock. Twice. The other one tripped.
Look, the realm's yours if you want it. Crown's on the hook. The ravens know the drill. Wake me when the screaming starts— or don't. I'll hear it anyway."""

DEFAULT_ENTRY_OUT = "/output/entry.txt"


def resolve_entry_path(raw: str) -> str:
    """Turn $ENTRY_OUT into a file path.

    The harness may hand us a file path (``/output/entry.txt``) or a
    directory (``/output``); in the latter case the entry lives at
    ``<dir>/entry.txt``.
    """
    if os.path.isdir(raw):
        return os.path.join(raw, "entry.txt")
    return raw


def main() -> int:
    entry_out = resolve_entry_path(os.environ.get("ENTRY_OUT") or DEFAULT_ENTRY_OUT)
    parent = os.path.dirname(entry_out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(entry_out, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    sys.stdout.write(ENTRY_TEXT + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
