import io
import json
import os
import logging
from typing import Optional

import openai

# Optional OCR dependencies: guard imports so the module can be imported in
# minimal environments (editor/type-checker friendly). If the libraries are
# missing, we provide clear runtime errors when OCR is actually requested.
try:
    import pytesseract  # type: ignore[import]
except Exception:
    pytesseract = None  # type: ignore[assignment]

try:
    from PIL import Image  # type: ignore[import]
except Exception:
    Image = None  # type: ignore[assignment]

try:
    from pdf2image import convert_from_bytes  # type: ignore[import]
except Exception:
    convert_from_bytes = None  # type: ignore[assignment]

from app.schemas.menu import MenuItem

logger = logging.getLogger(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


MENU_PARSER_PROMPT = """
You are a restaurant menu parser.

Convert the given menu text into STRICT JSON array.

Each item must contain:
- id (number)
- name (string)
- price (number)
- diet ("vegetarian" | "non-vegetarian")
- taste (list)
- health_flags (list)
- ingredients (list)

Do NOT add explanations.
Return ONLY JSON.
"""


async def parse_menu_from_file(file):
    content = await file.read()
    text = ""

    if file.content_type == "application/pdf":
        images = convert_from_bytes(content)
        for img in images:
            text += pytesseract.image_to_string(img)

    elif file.content_type.startswith("image/"):
        image = Image.open(io.BytesIO(content))
        text = pytesseract.image_to_string(image)

    else:
        raise ValueError("Unsupported file type")

    # 🔹 Convert text → structured JSON using LLM
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": MENU_PARSER_PROMPT},
            {"role": "user", "content": text}
        ],
    )

    raw = response.choices[0].message["content"]
    parsed = json.loads(raw)

    # Validate schema
    return [MenuItem(**item).dict() for item in parsed]
