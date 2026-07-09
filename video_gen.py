import os
import time
import math
import requests
from urllib.parse import quote
from PIL import Image
import imageio.v3 as iio

OUTPUT_DIR = "generated"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 300
VIDEO_FPS = 24
VIDEO_DURATION = 5  # seconds
VIDEO_WIDTH = 854
VIDEO_HEIGHT = 480

MOTION_PROMPT = (
    "Slow cinematic push-in, gentle camera movement, soft natural lighting, "
    "subtle premium product commercial feel, smooth realistic motion."
)


def create_campaign_video(image_path, product):
    """
    Generate a promotional video by creating a Ken Burns-style zoom/pan
    animation from the hero image. This creates a proper .mp4 video
    without needing a video generation API.
    """

    # Load the source image
    img = Image.open(image_path).convert("RGB")
    orig_w, orig_h = img.size

    # Calculate crop to fit 16:9
    target_ratio = VIDEO_WIDTH / VIDEO_HEIGHT
    img_ratio = orig_w / orig_h

    if img_ratio > target_ratio:
        # Image is wider — crop width
        new_w = int(orig_h * target_ratio)
        new_h = orig_h
        left = (orig_w - new_w) // 2
        top = 0
    else:
        # Image is taller — crop height
        new_w = orig_w
        new_h = int(orig_w / target_ratio)
        left = 0
        top = (orig_h - new_h) // 2

    img = img.crop((left, top, left + new_w, top + new_h))
    img = img.resize((VIDEO_WIDTH, VIDEO_HEIGHT), Image.LANCZOS)

    # Generate frames with Ken Burns effect (slow zoom-in)
    total_frames = VIDEO_FPS * VIDEO_DURATION
    frames = []

    for i in range(total_frames):
        t = i / total_frames  # 0 → 1

        # Zoom from 1.0 to 1.1 (slow push-in)
        zoom = 1.0 + 0.1 * t
        # Slight horizontal pan (left to right)
        pan_x = int(2 * VIDEO_WIDTH * t)

        # Crop and resize for zoom effect
        crop_w = int(VIDEO_WIDTH / zoom)
        crop_h = int(VIDEO_HEIGHT / zoom)
        cx = min(pan_x, VIDEO_WIDTH - crop_w)
        cy = (VIDEO_HEIGHT - crop_h) // 2

        frame = img.crop((cx, cy, cx + crop_w, cy + crop_h))
        frame = frame.resize((VIDEO_WIDTH, VIDEO_HEIGHT), Image.LANCZOS)
        frames.append(frame)

    # Write video
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(
        OUTPUT_DIR,
        f"{product.lower().replace(' ', '_')}_promo.mp4"
    )

    iio.imwrite(
        filepath,
        frames,
        fps=VIDEO_FPS,
        codec="libx264",
        output_params=["-pix_fmt", "yuv420p"],
    )

    return {"video_path": filepath, "motion_prompt": MOTION_PROMPT}
