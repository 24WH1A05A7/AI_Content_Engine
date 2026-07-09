# AI Content Engine

A multi-modal AI content generation application built with Streamlit.

The app accepts a simple product brief and generates an entire marketing campaign using multiple AI models.

---

## Features

✔ Campaign Tagline

✔ Blog Introduction

✔ Social Media Posts

✔ Hero Image

✔ Promotional Video

✔ Campaign Export

---

## Project Structure

content_engine/

├── app.py

├── config.py

├── text_gen.py

├── image_gen.py

├── video_gen.py

├── utils.py

├── requirements.txt

├── .env

├── generated/

└── assets/

---

## Installation

Clone the project

```bash
git clone <repo-url>
```

Go into the project

```bash
cd content_engine
```

Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Keys

Create a file named

```
.env
```

Example

```env
OPENROUTER_API_KEY=xxxxxxxx

OPENAI_API_KEY=xxxxxxxx

RUNWAY_API_KEY=xxxxxxxx
```

---

## Run

```bash
streamlit run app.py
```

---

## Workflow

1. Enter Product Name

2. Enter Target Audience

3. Choose Brand Tone

4. Click **Generate Campaign**

The application performs:

- Generate Campaign Tagline
- Generate Blog Introduction
- Generate Social Posts
- Generate Hero Image
- Generate Promotional Video

Everything is displayed automatically.

---

## Export

Generated assets are stored inside

```
generated/
```

Campaigns can also be exported as a ZIP archive.

---

## Models Used

### Text

OpenRouter

Model:

```
openai/gpt-4.1-mini
```

---

### Image

OpenAI GPT Image

Model:

```
gpt-image-1
```

---

### Video

Runway Gen-4 Image-to-Video

---

## Future Improvements

- Voice-over generation
- Multi-language support
- Multiple campaign variations
- Additional social platforms
- Campaign history
- PDF export
- Brand kit support
- Image editing

---

## License

MIT License