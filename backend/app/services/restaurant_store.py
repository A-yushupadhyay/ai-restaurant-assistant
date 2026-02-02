from typing import Dict
from app.schemas.restaurant import Restaurant


class RestaurantStore:
    def __init__(self):
        self._restaurants: Dict[str, Restaurant] = {}

    def add(self, restaurant: Restaurant):
        self._restaurants[restaurant.id] = restaurant

    def get(self, restaurant_id: str) -> Restaurant | None:
        return self._restaurants.get(restaurant_id)


restaurant_store = RestaurantStore()
