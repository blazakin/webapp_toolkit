# Could just use import qrcode, but that's not as fun, so we'll do our own later
from url_shorten import get_url, save_url
from PIL import Image, ImageDraw, ImageFont
import qrcode
import hashlib
import base64
import io
import os

_font_path = os.path.join(os.path.dirname(__file__), "resources", "LiberationSans-Regular.ttf")


def make_qr(data, add_shorten=False, domain=None):
    # Add shortened url
    # TODO send error if url cannot be added 
    key = None
    if add_shorten:
        key = str(hashlib.md5(data.encode()).hexdigest()[:4])
        # As this is a deterministic hash, check if this has been done before
        try:
            get_url(key)
        except KeyError:
            try: 
                save_url(key, data)
            except (ValueError, KeyError):
                key = None

    # Generate QR code
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Add shortened url to image
    if key is not None:
        # TODO return to domain once domain hosting has shorter or custom url
        # shortened_url = domain + "/S/" + key
        shortened_url =  "w7eg.net/S/" + key
        # Convert to gray scale image so the text looks better
        img = img.convert("L")
        width, height = img.size

        try:
            font = ImageFont.truetype(_font_path, 20)
        except IOError:
            font = ImageFont.load_default()

        # Check height of font
        draw = ImageDraw.Draw(img)
        bbox = draw.textbbox((0, 0), shortened_url, font=font)
        text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        top_margin = 0
        bottom_margin = 15
        new_height = height + top_margin + text_h + bottom_margin
        # Make new image with enough height
        # Then paste in the QR code and draw the text
        new_img = Image.new("L", (width, new_height), color=255)
        new_img.paste(img, (0, 0))
        draw = ImageDraw.Draw(new_img)
        text_x = (width - text_w) // 2
        text_y = height + top_margin
        draw.text((text_x,text_y), shortened_url, fill=0, font=font)
        img = new_img


    # Convert image to base64 string
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_str
