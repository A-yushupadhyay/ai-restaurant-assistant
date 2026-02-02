from typing import List
from app.schemas.menu import MenuItem
from app.schemas.context import ConversationContext


def filter_menu(menu: List[MenuItem], context: dict) -> List[MenuItem]:
    results = menu

    # Diet filter (hard rule)
    if context.get("diet"):
        results = [
            item for item in results
            if item.diet == context["diet"]
        ]

    # Budget filter (hard rule)
    if context.get("budget"):
        results = [
            item for item in results
            if item.price <= context["budget"]
        ]

    # Health filter (hard rule)
    if context.get("health"):
        for h in context["health"]:
            results = [
                item for item in results
                if h in item.health_flags
            ]

    # Taste filter (soft rule)
    if context.get("taste"):
        results = [
            item for item in results
            if any(t in item.taste for t in context["taste"])
        ]

    return results
