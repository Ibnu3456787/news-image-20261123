#!/usr/bin/env python3
"""Entrypoint for the news-image-20261123 make.fun bounty.

Copies the pre-built front page (entry.png, in this same directory)
into MAKEFUN_OUTPUT_DIR (default /output) as entry.png, after
validating it: PNG signature, size <= 1 MiB, dimensions <= 1024x1024
read from the IHDR chunk. The copy is verified by sha256.

Standard library only. No network. Never deletes the output
directory itself -- it only creates/writes the file inside it
(the grader mounts /bot read-only and /output writable, and runs
as an unprivileged user).
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1048576
MAX_DIM = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def read_entry():
    """Read entry.png from the directory this script lives in."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png")
    with open(path, "rb") as fh:
        return fh.read()


def validate(data):
    """Check the PNG signature, size and IHDR dimensions."""
    if len(data) > MAX_BYTES:
        return "entry.png is %d bytes, over the 1 MiB limit" % len(data)
    if len(data) < 33:
        return "entry.png is too short to be a PNG (%d bytes)" % len(data)
    if data[:8] != PNG_SIGNATURE:
        return "entry.png does not start with the PNG signature"
    chunk_len = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or chunk_len != 13:
        return "first PNG chunk is not a 13-byte IHDR"
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        return "entry.png is %dx%d, over the 1024x1024 limit" % (
            width, height)
    return None


def main():
    try:
        data = read_entry()
    except OSError as exc:
        return fail("cannot read entry.png next to main.py: %s" % exc)
    problem = validate(data)
    if problem:
        return fail(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return fail("cannot create output directory %r: %s" % (out_dir, exc))
    out_path = os.path.join(out_dir, "entry.png")
    try:
        with open(out_path, "wb") as fh:
            fh.write(data)
        with open(out_path, "rb") as fh:
            copied = fh.read()
    except OSError as exc:
        return fail("cannot write %r: %s" % (out_path, exc))
    if hashlib.sha256(copied).digest() != hashlib.sha256(data).digest():
        return fail("sha256 mismatch after copying entry.png")
    digest = hashlib.sha256(data).hexdigest()
    print("entry.png: %d bytes, sha256 %s" % (len(data), digest[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
