from pydantic import BaseModel
from typing import List, Optional


class MenuItem(BaseModel):
    id: int
    name: str
    price: int
    diet: str                 # vegetarian | non-vegetarian
    taste: List[str]          # spicy | sweet | mild
    health_flags: List[str]   # diabetic-friendly, low-oil
    ingredients: List[str]
