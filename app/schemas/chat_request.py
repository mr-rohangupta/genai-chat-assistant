from pydantic import BaseModel, Field
from typing import List
from app.schemas.chat_message import ChatMessage

class ChatRequest(BaseModel):

    message: str

    chat_history: List[ChatMessage] = Field(
        default_factory=list
    )