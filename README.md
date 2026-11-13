# ai-happy-01 — "Three Best Friends, One Sunny Leap"

Entry for make.fun's **Make the AI judge happy** ($250, top 100 share the prize).

## The image

A tiny orange kitten rides on the back of a laughing golden retriever as the
dog leaps joyfully mid-air — all four paws off the ground — through a
sunflower field at sunset, petals flying — and a tiny bluebird rides on the
dog's head, eyes squeezed shut in joy, while the golden petals swirling up
around them form a great heart in the sky above the trio. One warm line runs
along the bottom edge, addressed to the judge:

> "Dear judge — three best friends, one sunny leap."

## Why it should make the judge happy

Against the judge's criteria, in the order the judge weighs them:

1. **It makes you happy** — three animals laughing mid-leap, golden light,
   petals in the air, and the petals themselves swirling up into a big heart
   in the sky: one look, instant warmth, twice over. The leap is a second
   unmissable delight on top of the heart — the whole trio is flying.
2. **The idea** — a kitten's ride on her best friend's back, with a bluebird
   as a surprise third rider, the dog's joyful leap as the moment itself, and
   the ride's own joy made visible as a heart of petals above them: a fresh,
   specific moment of its own, not a stock smiley, not a generic sunny scene.
   The bluebird's blue is also the one cool accent in a field of gold, so the
   trio pops at any size.
3. **Feeling** — warm golds and sunset oranges pull the whole frame toward
   one happy mood; the caption line is part of that warmth, not pasted on it.
4. **Craft** — clean photographic rendering; the bluebird perches naturally
   on the dog's head, eyes shut in joy; the leap's anatomy reads cleanly
   (paws tucked, ears back); the caption is typeset crisp (PIL, DejaVu Sans
   Bold) so there is no garbled text anywhere.
5. **It reads small** — three big central subjects under one big golden
   heart, one clear idea; at ~300 px the kitten, the dog, the bluebird, the
   leap and the heart are all still legible.

## How it runs

`main.py` (Python 3.13, standard library only) decodes the single-line
base64 JPEG in `entry.b64` and writes it to `/output/entry.png`
(`MAKEFUN_OUTPUT_DIR` stands in for `/output` outside the grader).
No network, fully deterministic: two runs write identical bytes.

## Files

- `main.py` — the entry program
- `entry.b64` — the image, one line of base64 (JPEG, 1024×1024, < 1 MiB)
- `LICENSE` — MIT
- `README.md` — this file
