from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str
    restaurant_id: Optional[str] = None


class ChatResponse(BaseModel):
    session_id: str
    reply: str
    timestamp: datetime
    type: str  # "message" | "recommendation



