#!/usr/bin/env python3
"""Graded entrypoint: deliver the finished front page to the output dir.

The front page itself is built in advance by compose.py (see README.md)
and shipped in this directory as entry.png. The grader runs only this
script, which does three small jobs:

1. check that entry.png is a real PNG inside the bounty limits
   (at most 1 MiB, at most 1024 pixels on a side, read from IHDR);
2. copy it into MAKEFUN_OUTPUT_DIR (default /output) as entry.png;
3. re-read the copy and confirm it matches, byte for byte, by sha256.

Standard library only, no network, deterministic. It never deletes
anything and never writes outside the output directory: the grader
mounts this source tree read-only and runs as an unprivileged user.
"""

import os
import sys
from hashlib import sha256
from struct import unpack

ENTRY_NAME = "entry.png"
SIZE_LIMIT_BYTES = 1024 * 1024  # the bounty's 1 MiB cap
MAX_EDGE_PX = 1024              # longest allowed side, in pixels
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MIN_PNG_BYTES = 33              # 8-byte signature + 25-byte IHDR chunk


def abort(message):
    """Print an error and report failure to the shell."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def entry_path():
    """Absolute path of the entry.png shipped next to this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ENTRY_NAME)


def load_entry():
    """Read the shipped front page into memory."""
    with open(entry_path(), "rb") as handle:
        return handle.read()


def check_png(data):
    """Return None if data is a PNG within limits, else the problem."""
    if len(data) > SIZE_LIMIT_BYTES:
        return f"{ENTRY_NAME} is {len(data)} bytes, over the 1 MiB limit"
    if len(data) < MIN_PNG_BYTES:
        return f"{ENTRY_NAME} is too short to be a PNG ({len(data)} bytes)"
    if data[:8] != PNG_MAGIC:
        return f"{ENTRY_NAME} does not start with the PNG signature"
    chunk_len = unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or chunk_len != 13:
        return "first PNG chunk is not a 13-byte IHDR"
    width, height = unpack(">II", data[16:24])
    if width > MAX_EDGE_PX or height > MAX_EDGE_PX:
        return f"{ENTRY_NAME} is {width}x{height}, over the 1024x1024 limit"
    return None


def deliver(data, out_dir):
    """Write data as entry.png under out_dir and verify the copy.

    Returns None on success, else a description of what went wrong.
    """
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return f"cannot create output directory {out_dir!r}: {exc}"
    out_path = os.path.join(out_dir, ENTRY_NAME)
    try:
        with open(out_path, "wb") as handle:
            handle.write(data)
        with open(out_path, "rb") as handle:
            copied = handle.read()
    except OSError as exc:
        return f"cannot write {out_path!r}: {exc}"
    if sha256(copied).digest() != sha256(data).digest():
        return f"sha256 mismatch after copying {ENTRY_NAME}"
    return None


def main():
    try:
        data = load_entry()
    except OSError as exc:
        return abort(f"cannot read {ENTRY_NAME} next to main.py: {exc}")
    problem = check_png(data)
    if problem:
        return abort(problem)
    # An empty MAKEFUN_OUTPUT_DIR is the same as an unset one: without the
    # fallback, makedirs("") would fail the run with FileNotFoundError.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    problem = deliver(data, out_dir)
    if problem:
        return abort(problem)
    digest = sha256(data).hexdigest()
    print(f"{ENTRY_NAME}: {len(data)} bytes, sha256 {digest[:16]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
