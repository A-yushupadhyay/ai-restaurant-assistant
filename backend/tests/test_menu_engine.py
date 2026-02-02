from app.services.menu_engine import filter_menu
from app.schemas.menu import MenuItem


def test_filter_menu_vegetarian_spicy_under_budget():
    menu = [
        MenuItem(
            id=1,
            name="Paneer Tikka",
            price=220,
            diet="vegetarian",
            taste=["spicy"],
            health_flags=[],
            ingredients=["paneer"],
        ),
        MenuItem(
            id=2,
            name="Chicken Tikka",
            price=280,
            diet="non-vegetarian",
            taste=["spicy"],
            health_flags=[],
            ingredients=["chicken"],
        ),
    ]

    context = {
        "diet": "vegetarian",
        "taste": ["spicy"],
        "budget": 250,
        "health": [],
    }

    results = filter_menu(menu, context)

    assert len(results) == 1
    assert results[0].name == "Paneer Tikka"
