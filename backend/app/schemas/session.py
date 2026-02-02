from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str


class ChatResponse(BaseModel):
    session_id: str
    reply: str
    timestamp: datetime
