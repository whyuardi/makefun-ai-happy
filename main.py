"""ai-happy-01: "Three Best Friends, One Leap Through the Heart" (W42).

The picture lives in entry.b64 as one long base64 line. This program turns
it back into JPEG bytes and drops them at the grader's output path as
entry.png: a golden retriever leaping through a giant heart made of
sunflowers, an orange kitten riding along laughing, and a bluebird flying
beside them, with a warm line for the judge along the bottom edge.

Standard library only, no network, deterministic output.
"""

import base64
import os
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def picture_bytes():
    # The base64 blob is one line; the checks below guard the two JPEG
    # magic markers and the competition's 1 MiB size cap.
    encoded = (HERE / "entry.b64").read_text(encoding="ascii").strip()
    raw = base64.b64decode(encoded, validate=True)
    if raw[:2] != b"\xff\xd8":
        raise SystemExit("entry.b64 does not start with a JPEG header")
    if raw[-2:] != b"\xff\xd9":
        raise SystemExit("entry.b64 does not end with a JPEG trailer")
    if len(raw) > 1_048_576:
        raise SystemExit("entry is over the 1 MiB cap")
    return raw


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "entry.png").write_bytes(picture_bytes())


if __name__ == "__main__":
    run()
