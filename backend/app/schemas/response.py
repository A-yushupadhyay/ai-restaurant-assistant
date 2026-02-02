from pydantic import BaseModel
from typing import List


class DishExplanation(BaseModel):
    name: str
    price: int
    reasons: List[str]


class ResponseInput(BaseModel):
    dishes: List[DishExplanation]
    tone: str = "friendly"
