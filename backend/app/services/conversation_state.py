def resolve_state(context: dict) -> str:
    if not context.get("diet") and not context.get("taste"):
        return "discovery"

    if context.get("diet") and not context.get("budget"):
        return "narrowing"

    return "recommendation"
