#!/usr/bin/env python3
"""Entry point for the impossible-gadget catalogue photo.

Copies the bundled catalogue photograph (entry.png, next to this file)
to /output/entry.png so the grader can pick it up.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print(f"missing bundled image: {source}", file=sys.stderr)
        return 1

    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)
    size = os.path.getsize(destination)
    if size > 1_048_576:
        print(f"warning: {destination} is {size} bytes, over the 1 MiB limit", file=sys.stderr)
    print(f"wrote {destination} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
