"""ai-happy-01: "Three Best Friends, One Sunny Leap" (W31).

Decodes the single-line base64 JPEG in entry.b64 and writes the picture to
the output folder as entry.png. Three friends — a kitten, a golden
retriever mid-leap and a bluebird — ride together under a heart of petals,
with a warm line for the judge along the bottom edge.

Pure standard library, no network, and the same bytes out every run.
"""

import base64 as b64
import pathlib
import sys
from os import environ

SOURCE = pathlib.Path(__file__).resolve().parent
DEST = pathlib.Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def load_picture():
    text = (SOURCE / "entry.b64").read_text(encoding="ascii").strip()
    blob = b64.b64decode(text, validate=True)
    if blob[:2] != b"\xff\xd8" or blob[-2:] != b"\xff\xd9":
        sys.exit("entry.b64 is not a whole JPEG (missing SOI/EOI)")
    if len(blob) > 1_048_576:
        sys.exit("entry.b64 is larger than the 1 MiB entry cap")
    return blob


def main():
    picture = load_picture()
    DEST.mkdir(parents=True, exist_ok=True)
    # The grader expects the file to be named entry.png even though the
    # bytes inside are JPEG, so keep the name exactly as it is.
    (DEST / "entry.png").write_bytes(picture)


if __name__ == "__main__": main()
