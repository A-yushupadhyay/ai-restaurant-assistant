from pydantic import BaseModel
from typing import Optional


class Restaurant(BaseModel):
    id: str
    name: str
    cuisine: str
    theme_color: Optional[str] = "#0ea5e9"
