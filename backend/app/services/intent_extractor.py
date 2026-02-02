import os
import json
import openai
from app.schemas.intent import IntentResult
from app.config import AI_MODE

openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_intent(user_message: str, current_context: dict) -> IntentResult:
    # ✅ MOCK MODE (NO OPENAI, NO ERRORS)
    if AI_MODE == "mock":
        lowered = user_message.lower()
        updates = {}

        if "vegetarian" in lowered:
            updates["diet"] = "vegetarian"
        if "spicy" in lowered:
            updates.setdefault("taste", []).append("spicy")
        if "under" in lowered:
            for w in lowered.split():
                if w.isdigit():
                    updates["budget"] = int(w)

        return IntentResult(
            updates=updates,
            needs_clarification=False,
            clarification_questions=[],
        )

    # 🔴 REAL MODE (OPENAI)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Extract food preferences as JSON."},
                {"role": "user", "content": user_message},
            ],
            temperature=0,
        )

        data = json.loads(response.choices[0].message["content"])
        return IntentResult(**data)

    except openai.error.RateLimitError:
        # ✅ graceful degradation
        return IntentResult(
            updates={},
            needs_clarification=True,
            clarification_questions=[
                "I’m a bit busy right now 😅 Could you rephrase what you want?"
            ],
        )
