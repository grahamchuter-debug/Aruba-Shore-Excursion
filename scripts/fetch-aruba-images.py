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
# Prefer Aruba-tagged photos; avoid Cozumel jeep (bHavJvvmcAU) and Mayan ruins (PsgyWVeJjOA).
# Eagle Beach / lighthouse reuse within this site is intentional.
DOWNLOADS: list[tuple[str, str, int]] = [
    # Home hero: Eagle Beach sailboat sunset (Aruba)
    ("hero-aruba.png", "4jbbHRFjC8Y", 1920),
    # Best excursions: iconic Eagle Beach fofoti
    ("best-aruba-excursions.png", "WLD2CQuHVhU", 1920),
    # One day: Oranjestad palm street (not jeep slug)
    ("one-day-aruba.png", "YPIGSPOV3r4", 1920),
    # Eagle Beach fofoti (intentional reuse with best)
    ("eagle-beach-hero.png", "WLD2CQuHVhU", 1920),
    # Snorkeller with school of fish (distinct from shared SXM asset)
    ("aruba-snorkelling.png", "mFGqpEbrC1A", 1920),
    # California Lighthouse, Aruba
    ("aruba-island-tours.png", "x07QXWFgTVU", 1920),
    # Arid desert landscape for UTV / dry-side identity
    ("aruba-utv-adventures.png", "8vCQxoA5_oQ", 1920),
    # Natural pool / rocky coastline
    ("arikok-national-park.png", "aDsrhwXSjpA", 1920),
    ("california-lighthouse.png", "x07QXWFgTVU", 1920),
    # Private tours: Oranjestad colourful streetscape (not Mayan ruins)
    ("aruba-private-tours.png", "2_AU-j0ZrlM", 1920),
    # Family / beach day feel at Eagle Beach
    ("aruba-family.png", "fKORJlU4d9I", 1920),
    # Palm Beach chairs and turquoise water, Aruba
    ("aruba-beaches.png", "EdHmTaoQtlI", 1920),
    # Cruise passengers / Oranjestad near port
    ("aruba-faq.png", "PCLabewO7eE", 1920),
    # Intro: cactus overlooking turquoise water (dry landscape identity)
    ("aruba-intro.png", "AG_fwqAk19M", 1920),
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
