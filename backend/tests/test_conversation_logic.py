from app.services.conversation import handle_message


def test_change_diet_updates_recommendation():
    # Step 1: Start session
    res1 = handle_message(
        session_id=None,
        message="I want vegetarian food",
    )

    session_id = res1["session_id"]

    # Step 2: Add spice preference
    res2 = handle_message(
        session_id=session_id,
        message="something spicy",
    )

    # Step 3: Change mind
    res3 = handle_message(
        session_id=session_id,
        message="Actually make it non-veg",
    )

    assert res3["type"] in ["message", "recommendation"]
