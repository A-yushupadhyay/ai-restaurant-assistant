from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.conversation import handle_message

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = handle_message(
        session_id=request.session_id,
        message=request.message,
        restaurant_id=request.restaurant_id
    )
    return response


