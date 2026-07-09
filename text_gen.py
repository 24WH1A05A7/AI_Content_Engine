# ============================================================
# text_gen.py
# ============================================================

import json
import time
import requests

from config import (
    OPENROUTER_URL,
    HEADERS,
    TEXT_MODEL,
    MAX_RETRIES,
    REQUEST_TIMEOUT,
    DEFAULT_TEMPERATURE,
)


# ------------------------------------------------------------
# Helper: Call Pollinations.AI (free text generation)
# ------------------------------------------------------------

def call_llm(system_prompt, user_prompt, temperature=DEFAULT_TEMPERATURE):
    """
    Generic helper for calling OpenRouter (free tier).
    """

    payload = {
        "model": TEXT_MODEL,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    last_error = None

    for attempt in range(MAX_RETRIES):

        try:

            response = requests.post(
                OPENROUTER_URL,
                headers=HEADERS,
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )

            if response.status_code in (402, 429):
                raise RuntimeError(f"OpenRouter error {response.status_code}: {response.text[:100]}")

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"].strip()

        except Exception as e:
            last_error = e

            if attempt < MAX_RETRIES - 1:
                time.sleep(2)

    raise RuntimeError(f"LLM request failed: {last_error}")


# ------------------------------------------------------------
# Few-shot examples
# ------------------------------------------------------------

def get_fewshot_examples(tone):

    examples = {

        "playful": [
            (
                "Fruit Juice",
                "Kids",
                "Sip the Fun."
            ),
            (
                "Toy Robot",
                "Parents",
                "Smiles Built In."
            ),
        ],

        "premium": [
            (
                "Luxury Watch",
                "Professionals",
                "Time. Perfected."
            ),
            (
                "Leather Wallet",
                "Executives",
                "Crafted Beyond Expectations."
            ),
        ],

        "eco": [
            (
                "Bamboo Bottle",
                "Eco-conscious adults",
                "Refill Nature."
            ),
            (
                "Reusable Bag",
                "Families",
                "Carry Tomorrow."
            ),
        ],
    }

    return examples.get(tone.lower(), [])


# ------------------------------------------------------------
# Campaign Tagline
# ------------------------------------------------------------

def generate_tagline(product, audience, tone):

    system_prompt = "You are an award-winning creative director."

    user_prompt = (
        f"Generate one tagline (max 10 words) for {product} targeting {audience} with a {tone} tone. "
        f"No hashtags, no quotes, no explanation."
    )

    return call_llm(system_prompt, user_prompt)


# ------------------------------------------------------------
# Blog Introduction
# ------------------------------------------------------------

def generate_blog_intro(
    product,
    audience,
    tone,
    tagline,
):

    system_prompt = "You are an experienced content strategist."

    user_prompt = (
        f"Write a 200-word blog intro for {product} targeting {audience} ({tone} tone). "
        f"Use tagline naturally: \"{tagline}\". "
        f"Hook the reader, end with curiosity. No headings."
    )

    return call_llm(system_prompt, user_prompt)


# ------------------------------------------------------------
# Social Media Posts
# ------------------------------------------------------------

def generate_social_posts(
    product,
    audience,
    tone,
    tagline="",
):

    system_prompt = "You are a social media strategist. Return ONLY valid JSON."

    user_prompt = (
        f"Generate social posts for {product} targeting {audience} ({tone} tone). "
        f"Tagline: \"{tagline}\". "
        f"Return JSON with keys: twitter (max 280 chars), instagram (max 2200 chars), linkedin (max 700 chars). "
        f"No markdown, no code fences."
    )

    response = call_llm(system_prompt, user_prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except Exception:
        return {
            "twitter": "",
            "instagram": "",
            "linkedin": "",
        }


# ------------------------------------------------------------
# Generate Entire Text Suite
# ------------------------------------------------------------

def generate_text_assets(
    product,
    audience,
    tone,
):

    tagline = generate_tagline(
        product,
        audience,
        tone,
    )

    blog = generate_blog_intro(
        product,
        audience,
        tone,
        tagline,
    )

    social = generate_social_posts(
        product,
        audience,
        tone,
    )

    return {
        "tagline": tagline,
        "blog": blog,
        "social": social,
    }