import os
import time
import requests
from urllib.parse import quote

OUTPUT_DIR = "generated"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 120

# Pollinations.AI — completely free, no API key required
POLLINATIONS_URL = "https://image.pollinations.ai/prompt/{prompt}"

TONE_STYLES = {
    "playful":      "bright colorful product shot, fun cartoon-like setting, vivid saturated colors, cheerful playful mood, soft shadows",
    "premium":      "luxury product photography, dark moody background, cinematic rim lighting, shallow depth of field, sleek and elegant",
    "eco":          "natural daylight product shot, earthy tones, surrounded by leaves and greenery, organic warm feel, soft diffused light",
    "motivational": "bold dynamic product shot, dramatic directional lighting, high contrast, energetic atmosphere, dark gradient background",
    "professional": "clean corporate product photography, white or light grey studio background, even soft-box lighting, sharp focus",
}


def build_image_prompt(product, tagline, tone):
    style = TONE_STYLES.get(tone.lower(), "clean studio product photography, white background, soft even lighting")
    return (
        f"A high-quality commercial product advertisement photo of {product}. "
        f"{style}. "
        f"The product is the sole subject, centered in frame, filling most of the image. "
        f"16:9 aspect ratio. No text, no words, no labels, no watermarks, no logos. "
        f"No humans, no faces, no hands. Ultra-sharp product detail. "
        f"Award-winning product photography."
    )


def create_campaign_image(product, tagline, tone):
    prompt = build_image_prompt(product, tagline, tone)
    last_error = None

    encoded_prompt = quote(prompt)
    # seed makes results reproducible per product; turbo is faster and sharper for product shots
    seed = abs(hash(product + tone)) % 9999
    url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width=1280&height=720&nologo=true&enhance=true&model=flux&seed={seed}"
    )

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()

            # Pollinations returns the image directly as bytes
            if "image" not in response.headers.get("Content-Type", ""):
                raise RuntimeError(f"Unexpected content type: {response.headers.get('Content-Type')}")

            os.makedirs(OUTPUT_DIR, exist_ok=True)
            filepath = os.path.join(
                OUTPUT_DIR,
                f"{product.lower().replace(' ', '_')}_hero.png"
            )
            with open(filepath, "wb") as f:
                f.write(response.content)

            return {"image_path": filepath, "prompt": prompt}

        except Exception as e:
            last_error = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(2)

    raise RuntimeError(f"Image generation failed after {MAX_RETRIES} attempts: {last_error}")
