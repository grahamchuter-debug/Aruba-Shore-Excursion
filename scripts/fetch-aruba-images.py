#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

# Supplied locally; skipped by fetch (see images/ATTRIBUTION.md)
CUSTOM_IMAGES = frozenset({"aruba-cruise-port.png", "antilla-shipwreck.png"})

# output filename -> (Unsplash photo slug, width for download)
# Prefer Aruba-tagged photos where available; see images/ATTRIBUTION.md
DOWNLOADS: list[tuple[str, str, int]] = [
    # Home: Eagle Beach aerial, turquoise water (Aruba)
    ("hero-aruba.png", "vYXrNeIpm3w", 1920),
    # Best excursions collage-style: iconic Eagle Beach fofoti + water
    ("best-aruba-excursions.png", "WLD2CQuHVhU", 1920),
    # One day: Oranjestad colourful street / port area
    ("one-day-aruba.png", "bHavJvvmcAU", 1920),
    # Eagle Beach fofoti trees
    ("eagle-beach-hero.png", "WLD2CQuHVhU", 1920),
    # Snorkeller over coral reef
    ("aruba-snorkelling.png", "uTgKYNhuKOk", 1920),
    # California Lighthouse, Aruba
    ("aruba-island-tours.png", "x07QXWFgTVU", 1920),
    # UTV / desert adventure (Aruba's arid terrain)
    ("aruba-utv-adventures.png", "eXV74Ia7Log", 1920),
    # Natural pool / rocky coastline
    ("arikok-national-park.png", "aDsrhwXSjpA", 1920),
    ("california-lighthouse.png", "x07QXWFgTVU", 1920),
    # Private tour: scenic coastal drive vehicle
    ("aruba-private-tours.png", "PsgyWVeJjOA", 1920),
    # Family on sandy beach
    ("aruba-family.png", "BUIEgc7J0eo", 1920),
    # Palm Beach chairs and turquoise water, Aruba
    ("aruba-beaches.png", "Q0HR_nrDkB8", 1920),
    # Cruise passengers / Oranjestad near port
    ("aruba-faq.png", "PCLabewO7eE", 1920),
    # Intro: aerial Aruba coastline
    ("aruba-intro.png", "YZ8Jc6TiH2A", 1920),
]


def download(filename: str, slug: str, width: int) -> bool:
    dest = IMAGES / filename
    url = f"https://unsplash.com/photos/{slug}/download?force=true&w={width}"
    print(f"  {filename} <- {slug}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Aruba images from Unsplash…")
    if CUSTOM_IMAGES:
        print(f"  Skipping custom: {', '.join(sorted(CUSTOM_IMAGES))}")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if filename in CUSTOM_IMAGES:
            continue
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
