from fastapi import APIRouter

from app.schemas.chat_request import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    response = ChatService.chat(
        message=request.message,
        chat_history=request.chat_history
    )
    return{
        "response": response
    }