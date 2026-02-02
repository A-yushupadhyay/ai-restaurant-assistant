from pydantic import BaseModel
from typing import List, Optional, Dict


class IntentResult(BaseModel):
    intent: Optional[str] = "unknown"
    updates: Dict = {}
    needs_clarification: bool = False
    clarification_questions: List[str] = []
