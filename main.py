"""the-poster-for-a-place-that-i-2-20261121-0539 — VELMARA.

A travel poster for a place that does not exist: Velmara, a cliff-top
lighthouse town above a glowing turquoise bay at golden dusk, under two
moons, with white sailboats on calm luminous water. The invented place's
name is set into the picture in large cream serif capitals; there is no
other copy on the poster.

The entry image (entry.jpg, kept alongside this script) is the poster.
This script does one small, honest job: it copies the entry image, byte
for byte, to /output/entry.png so the competition runner can find it.
No network, no randomness, no arguments: the same input always writes
the same output.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.jpg"
DESTINATION = Path("/output/entry.png")


def load_entry_image() -> bytes:
    """Read entry.jpg next to this script; fail loudly if it is absent."""
    if not SOURCE.is_file():
        raise FileNotFoundError(
            f"entry image not found next to this script: {SOURCE}"
        )
    data = SOURCE.read_bytes()
    if not data:
        raise ValueError(f"entry image is empty: {SOURCE}")
    if not data.startswith(b"\xff\xd8\xff"):
        raise ValueError(f"entry image is not a JPEG: {SOURCE}")
    return data


def main() -> int:
    """Copy entry.jpg to /output/entry.png and report the size."""
    data = load_entry_image()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(data)
    print(f"Wrote {len(data)} bytes to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
