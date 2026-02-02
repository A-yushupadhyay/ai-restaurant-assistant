import os
import openai
from app.schemas.response import ResponseInput
from app.config import AI_MODE

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(data: ResponseInput) -> str:
    # ✅ MOCK MODE (NO OPENAI)
    if AI_MODE == "mock":
        lines = [
            f"- {d.name} (₹{d.price})"
            for d in data.dishes
        ]
        return (
            "Here are some good options for you 😊\n\n"
            + "\n".join(lines)
            + "\n\nWant something else?"
        )

    # 🔴 REAL MODE
    try:
        dish_text = "\n".join(
            f"- {d.name} (₹{d.price}) — {' & '.join(d.reasons)}"
            for d in data.dishes
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.4,
            messages=[
                {"role": "system", "content": "You are a friendly restaurant waiter."},
                {"role": "user", "content": dish_text},
            ],
        )

        return response.choices[0].message["content"]

    except openai.error.RateLimitError:
        return (
            "These dishes match your preferences 👍\n"
            "Let me know if you want to adjust anything."
        )
