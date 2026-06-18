from pydantic import BaseModel
from typing import List

from app.schemas.chat_message import ( ChatMessage )

class ChatRequest(BaseModel):

    message: str

    chat_history: List[ChatMessage] = []