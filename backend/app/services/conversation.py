import uuid
from datetime import datetime, timezone

from app.services.session_store import SessionStore
from app.schemas.context import ConversationContext
from app.services.menu_loader import load_menu
from app.services.menu_engine import filter_menu
from app.services.intent_extractor import extract_intent
from app.services.response_generator import generate_response
from app.schemas.response import DishExplanation, ResponseInput


session_store = SessionStore()


def handle_message(
    session_id: str | None,
    message: str,
    restaurant_id: str | None = None
):
    # 1️⃣ Session initialization
    if not session_id:
        session_id = str(uuid.uuid4())
        context = ConversationContext().model_dump()
        context["restaurant_id"] = restaurant_id
        context["last_recommendation_ids"] = []
        session_store.set(session_id, context)
    else:
        context = session_store.get(session_id)
        if not context:
            context = ConversationContext().model_dump()
            context["restaurant_id"] = restaurant_id
            context["last_recommendation_ids"] = []
            session_store.set(session_id, context)

    # 2️⃣ Intent extraction
    intent_result = extract_intent(message, context)

    # 3️⃣ Apply updates
    for key, value in intent_result.updates.items():
        if isinstance(value, list):
            context[key] = list(set(context.get(key, []) + value))
        else:
            context[key] = value

    session_store.set(session_id, context)

    # 4️⃣ Clarification
    if intent_result.needs_clarification:
        return {
            "session_id": session_id,
            "reply": "🤔 " + " ".join(intent_result.clarification_questions),
            "type": "message",
            "timestamp": datetime.now(timezone.utc),
        }

    # 🔑 NEW: are we ready to recommend?
    is_ready_for_recommendation = (
        context.get("diet")
        and (context.get("taste") or context.get("budget"))
    )

    # 🚦 5️⃣ Human waiter pacing (ONLY if NOT ready)
    if not is_ready_for_recommendation:
        if not context.get("diet"):
            return {
                "session_id": session_id,
                "reply": "Hey 😊 Welcome! Are you looking for vegetarian or non-veg today?",
                "type": "message",
                "timestamp": datetime.now(timezone.utc),
            }

        if not context.get("taste") and not context.get("budget"):
            return {
                "session_id": session_id,
                "reply": "Nice choice 👍 Any spice preference or budget I should keep in mind?",
                "type": "message",
                "timestamp": datetime.now(timezone.utc),
            }

    # 6️⃣ Menu recommendation (diff-aware)
    menu = load_menu()
    recommended = filter_menu(menu, context)

    if recommended:
        new_ids = [item.id for item in recommended[:3]]
        old_ids = context.get("last_recommendation_ids", [])

        # If recommendation did NOT change → light conversational reply
        if new_ids == old_ids:
            return {
                "session_id": session_id,
                "reply": "Got it 👍 I’ve updated that. Want to refine anything else?",
                "type": "message",
                "timestamp": datetime.now(timezone.utc),
            }

        # Recommendation changed → update memory
        context["last_recommendation_ids"] = new_ids
        session_store.set(session_id, context)

        dishes = [
            DishExplanation(
                name=item.name,
                price=item.price,
                reasons=[*item.taste, *item.health_flags],
            )
            for item in recommended[:3]
        ]

        reply = generate_response(
            ResponseInput(dishes=dishes, tone="friendly")
        )

        return {
            "session_id": session_id,
            "reply": reply,
            "type": "recommendation",
            "timestamp": datetime.now(timezone.utc),
        }

    # 7️⃣ Fallback
    return {
        "session_id": session_id,
        "reply": (
            "Hmm 🤔 I couldn’t find a perfect match.\n"
            "Want to tweak your preferences?"
        ),
        "type": "message",
        "timestamp": datetime.now(timezone.utc),
    }
