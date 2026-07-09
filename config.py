# ============================================================
# config.py
# ============================================================

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ------------------------------------------------------------
# API KEYS
# ------------------------------------------------------------

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY", "")


# ------------------------------------------------------------
# MODELS
# ------------------------------------------------------------

# Text model — OpenRouter free model
TEXT_MODEL = "nvidia/nemotron-nano-9b-v2:free"

# Image generation model
IMAGE_MODEL = "gpt-image-1"

# ------------------------------------------------------------
# OPENROUTER SETTINGS
# ------------------------------------------------------------

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "AI Content Engine"
}

# ------------------------------------------------------------
# OPENAI IMAGE SETTINGS
# ------------------------------------------------------------

OPENAI_IMAGE_URL = "https://api.openai.com/v1/images/generations"

IMAGE_HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# ------------------------------------------------------------
# RUNWAY SETTINGS
# ------------------------------------------------------------

RUNWAY_BASE_URL = "https://api.dev.runwayml.com/v1"

RUNWAY_HEADERS = {
    "Authorization": f"Bearer {RUNWAY_API_KEY}",
    "Content-Type": "application/json"
}

# ------------------------------------------------------------
# APP SETTINGS
# ------------------------------------------------------------

REQUEST_TIMEOUT = 120

MAX_RETRIES = 3

VIDEO_DURATION = 8

IMAGE_SIZE = "1536x1024"

DEFAULT_TEMPERATURE = 0.8

OUTPUT_DIR = "generated"

os.makedirs(OUTPUT_DIR, exist_ok=True)