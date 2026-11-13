#!/usr/bin/env python3
"""Build lightweight gallery images while preserving the archival master scans."""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = ROOT / "images"
ORIGINALS = (
    "TC-Ferns page 1.jpeg",
    "TC-Ferns page 2jpeg.jpeg",
    "TC-Ferns page 3.jpeg",
    "TC-Ferns page 4.jpeg",
    "TC-Ferns page 5.jpeg",
)
PAGE = ROOT / "_pages" / "research.md"

for number, filename in enumerate(ORIGINALS, start=1):
    source = IMAGE_DIR / filename
    destination = IMAGE_DIR / f"coal-ball-plate-{number}-web.jpg"
    if not source.is_file():
        raise FileNotFoundError(f"Missing original archival scan: {source}")
    with Image.open(source) as original:
        scan = ImageOps.exif_transpose(original).convert("RGB")
        scan.thumbnail((1800, 2400), Image.Resampling.LANCZOS)
        # Avoid aggressive chroma subsampling that can blur fine typed captions.
        scan.save(
            destination,
            "JPEG",
            quality=83,
            subsampling=0,
            optimize=True,
            progressive=True,
        )
    before = source.stat().st_size / 1048576
    after = destination.stat().st_size / 1048576
    print(f"Plate {number}: {before:.2f} MB -> {after:.2f} MB; {scan.size}")

html = PAGE.read_text(encoding="utf-8")
initial_img = 'src="{{ \'/images/TC-Ferns%20page%201.jpeg\' | relative_url }}"'
replacement_img = 'src="{{ \'/images/coal-ball-plate-1-web.jpg\' | relative_url }}"'
if initial_img in html:
    html = html.replace(initial_img, replacement_img, 1)
elif replacement_img not in html:
    raise RuntimeError("Could not find the initial gallery image markup.")

original_url_fn = "function pageUrl(i) { return base + encodeURIComponent(pages[i][0]); }"
preview_url_fn = original_url_fn + "\n      function previewUrl(i) { return base + 'coal-ball-plate-' + (i + 1) + '-web.jpg'; }"
if "function previewUrl(i)" not in html:
    if original_url_fn not in html:
        raise RuntimeError("Could not find the original page URL helper.")
    html = html.replace(original_url_fn, preview_url_fn)

html = html.replace("img.src = pageUrl(position);", "img.src = previewUrl(position);")
html = html.replace("const url = pageUrl(target);", "const url = previewUrl(target);")
html = html.replace("link.href = url;", "link.href = pageUrl(index);")

if "img.src = previewUrl(position);" not in html:
    raise RuntimeError("The preview preloading change did not apply.")
if "const url = previewUrl(target);" not in html:
    raise RuntimeError("The preview page-turn change did not apply.")
if "link.href = pageUrl(index);" not in html:
    raise RuntimeError("The full-resolution enlargement change did not apply.")

PAGE.write_text(html, encoding="utf-8")
print("Research gallery now uses compressed JPEGs for turning and original JPEGs for enlarging.")
