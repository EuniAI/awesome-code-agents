"""Promo utility: generate the repo's QR code (logo in the center) for posters, slides,
and talks. Run occasionally; the output docs/static/images/qr_code.png is committed.
Not part of the automation pipeline, and intentionally not referenced from the README."""

from PIL import Image, ImageDraw
import qrcode

# URL of your GitHub repo
url = "https://github.com/EuniAI/awesome-code-agents"

# Path to your icon (make sure the file exists)
from pathlib import Path
_HERE = Path(__file__).resolve().parent
icon_path = str(_HERE / "icon.png")

# Generate QR Code
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to allow center logo
    box_size=12,
    border=2,
)
qr.add_data(url)
qr.make()
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Open logo
icon = Image.open(icon_path).convert("RGBA")

# --- Crop to square (center crop) ---
w, h = icon.size
min_edge = min(w, h)
icon = icon.crop((
    (w - min_edge) // 2,
    (h - min_edge) // 2,
    (w + min_edge) // 2,
    (h + min_edge) // 2
))

# --- Resize logo ---
qr_w, qr_h = qr_img.size
logo_size = qr_w // 4
icon = icon.resize((logo_size, logo_size), Image.LANCZOS)

# --- Create white rounded background ---
pad = 18  # you can increase this for thicker border
bg_size = logo_size + pad*2
bg = Image.new("RGB", (bg_size, bg_size), "white")

# round corners mask
mask = Image.new("L", (bg_size, bg_size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle((0, 0, bg_size, bg_size), radius=bg_size//5, fill=255)

# Composite white rounded rectangle
bg = Image.composite(bg, Image.new("RGB", (bg_size, bg_size), "white"), mask)

# Paste logo centered on white rounded background
bg = bg.convert("RGBA")
icon = icon.convert("RGBA")
bg.paste(icon, (pad, pad), icon)

# --- Paste final logo block into QR ---
qr_img.paste(bg, ((qr_w - bg_size) // 2, (qr_h - bg_size) // 2))

# Save output
output_path = str(_HERE / "qr_code.png")
qr_img.save(output_path)

print(f"✅ Saved sleek QR code: {output_path}")
