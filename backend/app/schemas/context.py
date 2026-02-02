from pydantic import BaseModel
from typing import List, Optional


class ConversationContext(BaseModel):
    diet: Optional[str] = None
    health: List[str] = []
    taste: List[str] = []
    budget: Optional[int] = None
