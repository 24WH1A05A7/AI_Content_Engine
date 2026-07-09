# ============================================================
# utils.py
# ============================================================

import json
import os
import shutil
import zipfile
from datetime import datetime


# ============================================================
# Ensure Directory Exists
# ============================================================

def ensure_directory(path):

    if not os.path.exists(path):
        os.makedirs(path)


# ============================================================
# Safe JSON Loader
# ============================================================

_SOCIAL_FALLBACK = {"twitter": "", "instagram": "", "linkedin": ""}


def safe_json_load(text, fallback=None):
    """Parse JSON from LLM output, stripping markdown fences if needed.

    Returns a dict on success. If parsing still fails, returns `fallback`
    (defaults to an empty social-posts dict so callers never get None).
    """
    if fallback is None:
        fallback = dict(_SOCIAL_FALLBACK)

    if not text:
        return fallback

    try:
        return json.loads(text)

    except Exception:
        # Strip markdown code fences and retry
        cleaned = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(cleaned)

        except Exception:
            return fallback


# ============================================================
# Save Text File
# ============================================================

def save_text(filename, content):

    ensure_directory("generated")

    filepath = os.path.join(
        "generated",
        filename,
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


# ============================================================
# Save JSON File
# ============================================================

def save_json(filename, data):

    ensure_directory("generated")

    filepath = os.path.join(
        "generated",
        filename,
    )

    with open(filepath, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False,
        )

    return filepath


# ============================================================
# Timestamp
# ============================================================

def timestamp():

    return datetime.now().strftime("%Y%m%d_%H%M%S")


# ============================================================
# Create Campaign Folder
# ============================================================

def create_campaign_folder(product):

    folder = os.path.join(
        "generated",
        f"{product.replace(' ','_')}_{timestamp()}"
    )

    ensure_directory(folder)

    return folder


# ============================================================
# Copy File
# ============================================================

def copy_file(src, dst_folder):

    if not src:
        return

    shutil.copy(
        src,
        os.path.join(
            dst_folder,
            os.path.basename(src),
        ),
    )


# ============================================================
# Export Entire Campaign
# ============================================================

def export_campaign(
    folder,
    tagline,
    blog,
    social,
    image_path=None,
    video_path=None,
):

    save_text(
        os.path.join(
            os.path.basename(folder),
            "tagline.txt",
        ),
        tagline,
    )

    save_text(
        os.path.join(
            os.path.basename(folder),
            "blog_intro.txt",
        ),
        blog,
    )

    save_json(
        os.path.join(
            os.path.basename(folder),
            "social_posts.json",
        ),
        social,
    )

    if image_path:
        copy_file(
            image_path,
            folder,
        )

    if video_path:
        copy_file(
            video_path,
            folder,
        )

    return folder


# ============================================================
# Create ZIP
# ============================================================

def create_zip(folder):

    zip_path = folder + ".zip"

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED,
    ) as zipf:

        for root, _, files in os.walk(folder):

            for file in files:

                filepath = os.path.join(
                    root,
                    file,
                )

                arcname = os.path.relpath(
                    filepath,
                    folder,
                )

                zipf.write(
                    filepath,
                    arcname,
                )

    return zip_path


# ============================================================
# Cleanup Temporary Files
# ============================================================

def cleanup_generated(days_old=7):

    if not os.path.exists("generated"):
        return

    now = datetime.now().timestamp()

    for item in os.listdir("generated"):

        path = os.path.join(
            "generated",
            item,
        )

        try:

            modified = os.path.getmtime(path)

            age_days = (
                now - modified
            ) / (60 * 60 * 24)

            if age_days > days_old:

                if os.path.isdir(path):
                    shutil.rmtree(path)

                else:
                    os.remove(path)

        except Exception:
            pass