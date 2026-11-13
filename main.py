"""ai-happy-01 entry: "Three Best Friends, One Sunny Leap".

Writes one image to /output/entry.png: a tiny orange kitten riding on the
back of a laughing golden retriever leaping joyfully mid-air — all four paws
off the ground — through a sunflower field at sunset, with a tiny bluebird
riding on the dog's head — three best friends on one sunny leap — while the
golden petals swirling up around them form a great heart in the sky above,
and one warm line for the judge along the bottom edge.

The image is stored as a single line of base64 in entry.b64 (JPEG bytes).
The program is deterministic: the same input always produces the same
output bytes. Standard library only, no network.
"""
import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    payload = (HERE / "entry.b64").read_text(encoding="ascii").strip()
    data = base64.b64decode(payload, validate=True)
    # Guard: the payload must be a whole JPEG (SOI ... EOI), otherwise
    # fail loudly instead of writing a file the gate would refuse.
    if not (data[:2] == b"\xff\xd8" and data[-2:] == b"\xff\xd9"):
        raise ValueError("entry.b64 does not decode to a whole JPEG")
    # Guard: the gate caps the entry at 1 MiB, so refuse an oversize
    # payload here instead of writing a file the gate would refuse.
    if len(data) > 1_048_576:
        raise ValueError("entry.b64 decodes to more than 1 MiB")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
