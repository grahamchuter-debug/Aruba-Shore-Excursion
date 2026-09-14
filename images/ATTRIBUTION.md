# Image attribution

Site images are sourced from [Unsplash](https://unsplash.com) under the [Unsplash License](https://unsplash.com/license) (free for commercial and non-commercial use), except custom site-provided files noted below.

| File | Unsplash photo | Notes |
|------|----------------|-------|
| `hero-aruba.png` | [4jbbHRFjC8Y](https://unsplash.com/photos/4jbbHRFjC8Y) | Eagle Beach sailboat sunset, Aruba |
| `best-aruba-excursions.png` | [WLD2CQuHVhU](https://unsplash.com/photos/WLD2CQuHVhU) | Eagle Beach fofoti tree, Aruba |
| `aruba-cruise-port.png` | *(site-provided)* | Cruise ship at Oranjestad pier — custom photo |
| `one-day-aruba.png` | [YPIGSPOV3r4](https://unsplash.com/photos/YPIGSPOV3r4) | Oranjestad palm-lined street, Aruba |
| `eagle-beach-hero.png` | [WLD2CQuHVhU](https://unsplash.com/photos/WLD2CQuHVhU) | Eagle Beach, Aruba (intentional reuse) |
| `aruba-snorkelling.png` | [mFGqpEbrC1A](https://unsplash.com/photos/mFGqpEbrC1A) | Snorkeller with school of fish |
| `antilla-shipwreck.png` | *(site-provided)* | Aerial Antilla shipwreck with snorkelers — custom photo |
| `aruba-island-tours.png` | [x07QXWFgTVU](https://unsplash.com/photos/x07QXWFgTVU) | California Lighthouse, Aruba |
| `california-lighthouse.png` | [x07QXWFgTVU](https://unsplash.com/photos/x07QXWFgTVU) | California Lighthouse, Aruba (intentional reuse) |
| `aruba-private-tours.png` | [2_AU-j0ZrlM](https://unsplash.com/photos/2_AU-j0ZrlM) | Colourful Oranjestad streetscape (not ruins) |
| `aruba-family.png` | [fKORJlU4d9I](https://unsplash.com/photos/fKORJlU4d9I) | Eagle Beach, Aruba |
| `aruba-beaches.png` | [EdHmTaoQtlI](https://unsplash.com/photos/EdHmTaoQtlI) | Palm Beach loungers, Aruba |
| `aruba-faq.png` | [PCLabewO7eE](https://unsplash.com/photos/PCLabewO7eE) | Oranjestad near Aruba Ports Authority |
| `aruba-intro.png` | [AG_fwqAk19M](https://unsplash.com/photos/AG_fwqAk19M) | Cactus overlooking turquoise water — dry landscape identity |

**Integrity note:** Replaced assets that previously matched Cozumel (`bHavJvvmcAU` jeep, `PsgyWVeJjOA` Mayan ruins) or St Maarten shared hashes. Eagle Beach and lighthouse images may be reused deliberately within this site only.

Re-download after changing sources:

```bash
python3 scripts/fetch-aruba-images.py
```

The build script does not overwrite existing images in `images/`.

**Phase 31B:** Removed `arikok-national-park.png` (wrong geography) and `aruba-utv-adventures.png` (misleading continental desert). Arikok/UTV pages now use `aruba-intro.png`.
