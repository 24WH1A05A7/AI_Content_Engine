# import streamlit as st

# from text_gen import generate_tagline, generate_blog_intro, generate_social_posts
# from image_gen import create_campaign_image
# from video_gen import create_campaign_video
# from utils import create_campaign_folder, export_campaign, create_zip

# st.set_page_config(page_title="AI Content Engine", layout="wide")
# st.title("🚀 AI Content Engine")

# # ── Sidebar ──────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.header("Campaign Brief")
#     product  = st.text_input("Product Name",    placeholder="e.g. Smart Water Bottle")
#     audience = st.text_input("Target Audience", placeholder="e.g. Fitness enthusiasts")
#     tone     = st.selectbox("Brand Tone", ["Playful", "Premium", "Eco", "Motivational", "Professional"])
#     generate = st.button("Generate Campaign", type="primary", use_container_width=True)

# # ── Main layout ───────────────────────────────────────────────────────────────
# left, right = st.columns(2)

# if generate:
#     if not product or not audience:
#         st.warning("Please fill in Product Name and Target Audience.")
#         st.stop()

#     # ── Text assets (left column) ─────────────────────────────────────────────
#     with left:
#         with st.spinner("Generating tagline…"):
#             tagline = generate_tagline(product, audience, tone)
#         st.subheader("🏷️ Campaign Tagline")
#         st.success(tagline)

#         with st.spinner("Writing blog introduction…"):
#             blog = generate_blog_intro(product, audience, tone, tagline)
#         st.subheader("📝 Blog Introduction")
#         st.write(blog)

#         with st.spinner("Crafting social posts…"):
#             social = generate_social_posts(product, audience, tone, tagline)
#         st.subheader("📱 Social Media Posts")
#         st.markdown(f"**Twitter / X**\n\n{social.get('twitter','')}")
#         st.markdown(f"**Instagram**\n\n{social.get('instagram','')}")
#         st.markdown(f"**LinkedIn**\n\n{social.get('linkedin','')}")

#     # ── Visual assets (right column) ──────────────────────────────────────────
#     with right:
#         with st.spinner("Generating hero image…"):
#             img_result = create_campaign_image(product, tagline, tone)
#         st.subheader("🖼️ Hero Image")
#         st.image(img_result["image_path"], use_container_width=True)

#         with st.spinner("Generating promotional video…"):
#             try:
#                 vid_result = create_campaign_video(img_result["image_path"], product)
#                 st.subheader("🎬 Promotional Video")
#                 st.video(vid_result["video_path"])
#             except Exception as e:
#                 st.error(f"Video generation failed: {e}")
#                 vid_result = None

#     # ── Export ────────────────────────────────────────────────────────────────
#     st.divider()
#     folder = create_campaign_folder(product)
#     export_campaign(
#         folder, tagline, blog, social,
#         img_result["image_path"],
#         vid_result["video_path"] if vid_result else None,
#     )
#     zip_path = create_zip(folder)

#     with open(zip_path, "rb") as f:
#         st.download_button(
#             "⬇️ Download Campaign ZIP",
#             data=f,
#             file_name=f"{product.replace(' ','_')}_campaign.zip",
#             mime="application/zip",
#             use_container_width=True,
#         )


# import streamlit as st

# from text_gen import generate_tagline, generate_blog_intro, generate_social_posts
# from image_gen import create_campaign_image
# from video_gen import create_campaign_video
# from utils import create_campaign_folder, export_campaign, create_zip

# st.set_page_config(page_title="AI Content Engine", page_icon="🚀", layout="wide")

# # ── Theme ──────────────────────────────────────────────────────────────────
# # Ink navy + amber spark accent, teal for "visual" outputs.
# # Space Grotesk for headings (distinct, geometric), Inter for body/UI.
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');

# :root {
#     --ink:        #10172A;
#     --ink-soft:   #2A3350;
#     --canvas:     #F6F7FB;
#     --card:       #FFFFFF;
#     --border:     #E7E9F2;
#     --muted:      #6B7280;
#     --amber:      #FF6B4A;
#     --amber-soft: #FFE7DE;
#     --teal:       #17A98C;
#     --teal-soft:  #DFF6EF;
#     --text:       #1B2033;
# }

# html, body, [class*="css"]  {
#     font-family: 'Inter', sans-serif;
#     color: var(--text);
# }

# .stApp {
#     background: var(--canvas);
# }

# h1, h2, h3, h4, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
#     font-family: 'Space Grotesk', sans-serif !important;
#     color: var(--ink) !important;
#     letter-spacing: -0.01em;
# }

# /* ── App title ──────────────────────────────────────────────────────── */
# .app-hero {
#     display: flex;
#     align-items: center;
#     gap: 14px;
#     padding: 4px 0 4px 0;
#     margin-bottom: 4px;
# }
# .app-hero .badge {
#     font-family: 'Space Grotesk', sans-serif;
#     font-size: 0.72rem;
#     font-weight: 700;
#     letter-spacing: 0.08em;
#     text-transform: uppercase;
#     color: var(--amber);
#     background: var(--amber-soft);
#     padding: 4px 10px;
#     border-radius: 999px;
# }
# .app-hero h1 {
#     font-size: 2rem !important;
#     margin: 0 !important;
# }
# .app-sub {
#     color: var(--muted);
#     font-size: 0.98rem;
#     margin-top: -6px;
#     margin-bottom: 18px;
# }

# /* ── Sidebar ────────────────────────────────────────────────────────── */
# section[data-testid="stSidebar"] {
#     background: var(--ink);
#     border-right: 1px solid var(--border);
# }
# section[data-testid="stSidebar"] * {
#     color: #E9ECF6 !important;
# }
# section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h1 {
#     font-family: 'Space Grotesk', sans-serif !important;
#     color: #FFFFFF !important;
# }
# section[data-testid="stSidebar"] .stTextInput input,
# section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
#     background: var(--ink-soft) !important;
#     border: 1px solid #3A4468 !important;
#     color: #FFFFFF !important;
#     border-radius: 8px !important;
# }
# section[data-testid="stSidebar"] label {
#     font-weight: 600 !important;
#     font-size: 0.85rem !important;
#     color: #B9C0DA !important;
#     text-transform: uppercase;
#     letter-spacing: 0.03em;
# }
# section[data-testid="stSidebar"] hr {
#     border-color: #3A4468;
# }

# /* Sidebar primary button = the spark */
# section[data-testid="stSidebar"] .stButton button {
#     background: var(--amber) !important;
#     color: #10172A !important;
#     border: none !important;
#     font-weight: 700 !important;
#     font-family: 'Space Grotesk', sans-serif !important;
#     border-radius: 8px !important;
#     padding: 0.7rem 1rem !important;
#     letter-spacing: 0.01em;
#     transition: transform 0.05s ease-in-out, box-shadow 0.15s ease-in-out;
#     box-shadow: 0 4px 14px rgba(255, 107, 74, 0.25);
# }
# section[data-testid="stSidebar"] .stButton button:hover {
#     box-shadow: 0 6px 18px rgba(255, 107, 74, 0.4);
#     transform: translateY(-1px);
# }

# /* ── Cards ──────────────────────────────────────────────────────────── */
# div[data-testid="stVerticalBlockBorderWrapper"] {
#     background: var(--card);
#     border-radius: 12px !important;
#     border: 1px solid var(--border) !important;
#     box-shadow: 0 1px 3px rgba(16, 23, 42, 0.04);
#     padding: 4px;
# }
# /* Force readable text inside cards regardless of light/dark theme setting */
# div[data-testid="stVerticalBlockBorderWrapper"] p,
# div[data-testid="stVerticalBlockBorderWrapper"] span,
# div[data-testid="stVerticalBlockBorderWrapper"] li,
# div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stMarkdownContainer"] {
#     color: var(--text) !important;
# }

# .section-eyebrow {
#     font-family: 'Space Grotesk', sans-serif;
#     font-size: 0.72rem;
#     font-weight: 700;
#     letter-spacing: 0.09em;
#     text-transform: uppercase;
#     padding: 3px 10px;
#     border-radius: 999px;
#     display: inline-block;
#     margin-bottom: 6px;
# }
# .eyebrow-text  { color: var(--amber); background: var(--amber-soft); }
# .eyebrow-visual{ color: var(--teal);  background: var(--teal-soft); }

# .card-title {
#     font-family: 'Space Grotesk', sans-serif;
#     font-size: 1.15rem;
#     font-weight: 700;
#     color: var(--ink);
#     margin: 0 0 10px 0;
# }

# /* Tagline highlight */
# .tagline-box {
#     background: linear-gradient(135deg, var(--amber-soft), #FFFFFF);
#     border: 1px solid var(--amber);
#     border-radius: 10px;
#     padding: 14px 16px;
#     font-size: 1.15rem;
#     font-weight: 600;
#     font-family: 'Space Grotesk', sans-serif;
#     color: var(--ink);
# }

# /* Social post cards */
# .social-card {
#     border: 1px solid var(--border);
#     border-radius: 10px;
#     padding: 12px 14px;
#     margin-bottom: 10px;
#     background: #FCFCFE;
#     color: var(--text);
# }
# .social-platform {
#     font-family: 'Space Grotesk', sans-serif;
#     font-weight: 700;
#     font-size: 0.85rem;
#     color: var(--ink);
#     margin-bottom: 4px;
#     display: block;
# }

# /* Buttons in main area (download) */
# .stDownloadButton button {
#     background: var(--ink) !important;
#     color: #FFFFFF !important;
#     font-family: 'Space Grotesk', sans-serif !important;
#     font-weight: 700 !important;
#     border-radius: 8px !important;
#     border: none !important;
#     padding: 0.75rem 1rem !important;
# }
# .stDownloadButton button:hover {
#     background: var(--ink-soft) !important;
# }

# hr { border-color: var(--border); }

# /* Empty state */
# .empty-state {
#     border: 1.5px dashed var(--border);
#     border-radius: 14px;
#     padding: 48px 32px;
#     text-align: center;
#     color: var(--muted);
#     background: var(--card);
# }
# .empty-state .big {
#     font-family: 'Space Grotesk', sans-serif;
#     font-size: 1.3rem;
#     color: var(--ink);
#     font-weight: 600;
#     margin-bottom: 6px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── Sidebar ──────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("## 🚀 Campaign Brief")
#     st.caption("Tell us about the product — we'll spin up a full campaign.")
#     st.markdown("---")
#     product  = st.text_input("Product Name",    placeholder="e.g. Smart Water Bottle")
#     audience = st.text_input("Target Audience", placeholder="e.g. Fitness enthusiasts")
#     tone     = st.selectbox("Brand Tone", ["Playful", "Premium", "Eco", "Motivational", "Professional"])
#     st.markdown("<br>", unsafe_allow_html=True)
#     generate = st.button("✨ Generate Campaign", type="primary", use_container_width=True)

# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="app-hero">
#     <h1>AI Content Engine</h1>
#     <span class="badge">Beta</span>
# </div>
# <div class="app-sub">Generate on-brand taglines, copy, and visuals for a full marketing campaign in one click.</div>
# """, unsafe_allow_html=True)

# # ── Main layout ───────────────────────────────────────────────────────────────
# left, right = st.columns(2)

# if generate:
#     if not product or not audience:
#         st.warning("Please fill in Product Name and Target Audience.")
#         st.stop()

#     # ── Text assets (left column) ─────────────────────────────────────────────
#     with left:
#         with st.container(border=True):
#             st.markdown('<span class="section-eyebrow eyebrow-text">Text</span>', unsafe_allow_html=True)
#             st.markdown('<div class="card-title">🏷️ Campaign Tagline</div>', unsafe_allow_html=True)
#             with st.spinner("Generating tagline…"):
#                 tagline = generate_tagline(product, audience, tone)
#             st.markdown(f'<div class="tagline-box">{tagline}</div>', unsafe_allow_html=True)

#         with st.container(border=True):
#             st.markdown('<span class="section-eyebrow eyebrow-text">Text</span>', unsafe_allow_html=True)
#             st.markdown('<div class="card-title">📝 Blog Introduction</div>', unsafe_allow_html=True)
#             with st.spinner("Writing blog introduction…"):
#                 blog = generate_blog_intro(product, audience, tone, tagline)
#             st.write(blog)

#         with st.container(border=True):
#             st.markdown('<span class="section-eyebrow eyebrow-text">Text</span>', unsafe_allow_html=True)
#             st.markdown('<div class="card-title">📱 Social Media Posts</div>', unsafe_allow_html=True)
#             with st.spinner("Crafting social posts…"):
#                 social = generate_social_posts(product, audience, tone, tagline)
#             st.markdown(f"""
#             <div class="social-card"><span class="social-platform">Twitter / X</span>{social.get('twitter','')}</div>
#             <div class="social-card"><span class="social-platform">Instagram</span>{social.get('instagram','')}</div>
#             <div class="social-card"><span class="social-platform">LinkedIn</span>{social.get('linkedin','')}</div>
#             """, unsafe_allow_html=True)

#     # ── Visual assets (right column) ──────────────────────────────────────────
#     with right:
#         with st.container(border=True):
#             st.markdown('<span class="section-eyebrow eyebrow-visual">Visual</span>', unsafe_allow_html=True)
#             st.markdown('<div class="card-title">🖼️ Hero Image</div>', unsafe_allow_html=True)
#             with st.spinner("Generating hero image…"):
#                 img_result = create_campaign_image(product, tagline, tone)
#             st.image(img_result["image_path"], use_container_width=True)

#         with st.container(border=True):
#             st.markdown('<span class="section-eyebrow eyebrow-visual">Visual</span>', unsafe_allow_html=True)
#             st.markdown('<div class="card-title">🎬 Promotional Video</div>', unsafe_allow_html=True)
#             with st.spinner("Generating promotional video…"):
#                 try:
#                     vid_result = create_campaign_video(img_result["image_path"], product)
#                     st.video(vid_result["video_path"])
#                 except Exception as e:
#                     st.error(f"Video generation failed: {e}")
#                     vid_result = None

#     # ── Export ────────────────────────────────────────────────────────────────
#     st.divider()
#     folder = create_campaign_folder(product)
#     export_campaign(
#         folder, tagline, blog, social,
#         img_result["image_path"],
#         vid_result["video_path"] if vid_result else None,
#     )
#     zip_path = create_zip(folder)

#     with open(zip_path, "rb") as f:
#         st.download_button(
#             "⬇️ Download Campaign ZIP",
#             data=f,
#             file_name=f"{product.replace(' ','_')}_campaign.zip",
#             mime="application/zip",
#             use_container_width=True,
#         )
# else:
#     st.markdown("""
#     <div class="empty-state">
#         <div class="big">Your campaign will appear here</div>
#         Fill in the brief on the left and hit <b>Generate Campaign</b> to create a tagline,
#         blog intro, social posts, hero image, and promo video — all in one pass.
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st

from text_gen import generate_tagline, generate_blog_intro, generate_social_posts
from image_gen import create_campaign_image
from video_gen import create_campaign_video
from utils import create_campaign_folder, export_campaign, create_zip

st.set_page_config(page_title="AI Content Engine", page_icon="🚀", layout="wide")

# ── Theme ──────────────────────────────────────────────────────────────────
# Ink navy + amber spark accent, teal for "visual" outputs.
# Space Grotesk for headings (distinct, geometric), Inter for body/UI.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --ink:        #10172A;
    --ink-soft:   #2A3350;
    --canvas:     #F6F7FB;
    --card:       #FFFFFF;
    --border:     #E7E9F2;
    --muted:      #6B7280;
    --amber:      #FF6B4A;
    --amber-soft: #FFE7DE;
    --teal:       #17A98C;
    --teal-soft:  #DFF6EF;
    --text:       #1B2033;
}

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    color: var(--text);
}

.stApp {
    background: var(--canvas);
}

/* Force readable dark text everywhere in the main content area, regardless
   of the user's light/dark Streamlit theme setting or internal testid
   changes between Streamlit versions. Accent-colored elements below all use
   !important so they still win over this reset. */
[data-testid="stMain"] p,
[data-testid="stMain"] span,
[data-testid="stMain"] li,
[data-testid="stMain"] label,
[data-testid="stMain"] div,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] * {
    color: var(--text) !important;
}

h1, h2, h3, h4, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--ink) !important;
    letter-spacing: -0.01em;
}

/* ── App title ──────────────────────────────────────────────────────── */
.app-hero {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 4px 0 4px 0;
    margin-bottom: 4px;
}
.app-hero .badge {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--amber) !important;
    background: var(--amber-soft);
    padding: 4px 10px;
    border-radius: 999px;
}
.app-hero h1 {
    font-size: 2rem !important;
    margin: 0 !important;
}
.app-sub {
    color: var(--muted);
    font-size: 0.98rem;
    margin-top: -6px;
    margin-bottom: 18px;
}

/* ── Sidebar ────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: var(--ink);
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] * {
    color: #E9ECF6 !important;
}
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h1 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #FFFFFF !important;
}
section[data-testid="stSidebar"] .stTextInput input,
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
    background: var(--ink-soft) !important;
    border: 1px solid #3A4468 !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
}
section[data-testid="stSidebar"] label {
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    color: #B9C0DA !important;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}
section[data-testid="stSidebar"] hr {
    border-color: #3A4468;
}

/* Sidebar primary button = the spark */
section[data-testid="stSidebar"] .stButton button {
    background: var(--amber) !important;
    color: #10172A !important;
    border: none !important;
    font-weight: 700 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    border-radius: 8px !important;
    padding: 0.7rem 1rem !important;
    letter-spacing: 0.01em;
    transition: transform 0.05s ease-in-out, box-shadow 0.15s ease-in-out;
    box-shadow: 0 4px 14px rgba(255, 107, 74, 0.25);
}
section[data-testid="stSidebar"] .stButton button:hover {
    box-shadow: 0 6px 18px rgba(255, 107, 74, 0.4);
    transform: translateY(-1px);
}

/* ── Cards ──────────────────────────────────────────────────────────── */
/* Streamlit's bordered-container testid has changed across versions, so
   target both the current and legacy names to stay robust. */
div[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stVerticalBlock"]:has(> div[style*="border"]) {
    background: var(--card);
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    box-shadow: 0 1px 3px rgba(16, 23, 42, 0.04);
    padding: 4px;
}

.section-eyebrow {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 999px;
    display: inline-block;
    margin-bottom: 6px;
}
.eyebrow-text  { color: var(--amber) !important; background: var(--amber-soft); }
.eyebrow-visual{ color: var(--teal) !important;  background: var(--teal-soft); }

.card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--ink) !important;
    margin: 0 0 10px 0;
}

/* Tagline highlight */
.tagline-box {
    background: linear-gradient(135deg, var(--amber-soft), #FFFFFF);
    border: 1px solid var(--amber);
    border-radius: 10px;
    padding: 14px 16px;
    font-size: 1.15rem;
    font-weight: 600;
    font-family: 'Space Grotesk', sans-serif;
    color: var(--ink) !important;
}

/* Social post cards */
.social-card {
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 10px;
    background: #FCFCFE;
    color: var(--text) !important;
}
.social-card * {
    color: var(--text) !important;
}
.social-platform {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    color: var(--ink) !important;
    margin-bottom: 4px;
    display: block;
}

/* Buttons in main area (download) */
.stDownloadButton button,
.stDownloadButton button * {
    background: var(--ink) !important;
    color: #FFFFFF !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 0.75rem 1rem !important;
}
.stDownloadButton button:hover {
    background: var(--ink-soft) !important;
}

hr { border-color: var(--border); }

/* Empty state */
.empty-state {
    border: 1.5px dashed var(--border);
    border-radius: 14px;
    padding: 48px 32px;
    text-align: center;
    color: var(--muted) !important;
    background: var(--card);
}
.empty-state * {
    color: var(--muted) !important;
}
.empty-state .big {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.3rem;
    color: var(--ink) !important;
    font-weight: 600;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🚀 Campaign Brief")
    st.caption("Tell us about the product — we'll spin up a full campaign.")
    st.markdown("---")
    product  = st.text_input("Product Name",    placeholder="e.g. Smart Water Bottle")
    audience = st.text_input("Target Audience", placeholder="e.g. Fitness enthusiasts")
    tone     = st.selectbox("Brand Tone", ["Playful", "Premium", "Eco", "Motivational", "Professional"])
    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("✨ Generate Campaign", type="primary", use_container_width=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-hero">
    <h1>AI Content Engine</h1>
    <span class="badge">Beta</span>
</div>
<div class="app-sub">Generate on-brand taglines, copy, and visuals for a full marketing campaign in one click.</div>
""", unsafe_allow_html=True)

# ── Main layout ───────────────────────────────────────────────────────────────
left, right = st.columns(2)

if generate:
    if not product or not audience:
        st.warning("Please fill in Product Name and Target Audience.")
        st.stop()

    # ── Text assets (left column) ─────────────────────────────────────────────
    with left:
        with st.container(border=True):
            st.markdown('<span class="section-eyebrow eyebrow-text">Text</span>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🏷️ Campaign Tagline</div>', unsafe_allow_html=True)
            with st.spinner("Generating tagline…"):
                tagline = generate_tagline(product, audience, tone)
            st.markdown(f'<div class="tagline-box">{tagline}</div>', unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown('<span class="section-eyebrow eyebrow-text">Text</span>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📝 Blog Introduction</div>', unsafe_allow_html=True)
            with st.spinner("Writing blog introduction…"):
                blog = generate_blog_intro(product, audience, tone, tagline)
            st.write(blog)

        with st.container(border=True):
            st.markdown('<span class="section-eyebrow eyebrow-text">Text</span>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📱 Social Media Posts</div>', unsafe_allow_html=True)
            with st.spinner("Crafting social posts…"):
                social = generate_social_posts(product, audience, tone, tagline)
            st.markdown(f"""
            <div class="social-card"><span class="social-platform">Twitter / X</span>{social.get('twitter','')}</div>
            <div class="social-card"><span class="social-platform">Instagram</span>{social.get('instagram','')}</div>
            <div class="social-card"><span class="social-platform">LinkedIn</span>{social.get('linkedin','')}</div>
            """, unsafe_allow_html=True)

    # ── Visual assets (right column) ──────────────────────────────────────────
    with right:
        with st.container(border=True):
            st.markdown('<span class="section-eyebrow eyebrow-visual">Visual</span>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🖼️ Hero Image</div>', unsafe_allow_html=True)
            with st.spinner("Generating hero image…"):
                img_result = create_campaign_image(product, tagline, tone)
            st.image(img_result["image_path"], use_container_width=True)

        with st.container(border=True):
            st.markdown('<span class="section-eyebrow eyebrow-visual">Visual</span>', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🎬 Promotional Video</div>', unsafe_allow_html=True)
            with st.spinner("Generating promotional video…"):
                try:
                    vid_result = create_campaign_video(img_result["image_path"], product)
                    st.video(vid_result["video_path"])
                except Exception as e:
                    st.error(f"Video generation failed: {e}")
                    vid_result = None

    # ── Export ────────────────────────────────────────────────────────────────
    st.divider()
    folder = create_campaign_folder(product)
    export_campaign(
        folder, tagline, blog, social,
        img_result["image_path"],
        vid_result["video_path"] if vid_result else None,
    )
    zip_path = create_zip(folder)

    with open(zip_path, "rb") as f:
        st.download_button(
            "⬇️ Download Campaign ZIP",
            data=f,
            file_name=f"{product.replace(' ','_')}_campaign.zip",
            mime="application/zip",
            use_container_width=True,
        )
else:
    st.markdown("""
    <div class="empty-state">
        <div class="big">Your campaign will appear here</div>
        Fill in the brief on the left and hit <b>Generate Campaign</b> to create a tagline,
        blog intro, social posts, hero image, and promo video — all in one pass.
    </div>
    """, unsafe_allow_html=True)