from uuid import uuid4
from app.services.memory_extractor_service import MemoryExtractorService
from app.services.memory_service import MemoryService
from app.services.rag_service import (
    RAGService
)


class ChatService:

    @staticmethod
    def chat(
            message: str,
            chat_history: list
    ):
        history_text = ""

        for chat in chat_history:
            history_text += (
                f"{chat.role}: "
                f"{chat.content}\n"
            )

        prompt = f"""
        You are a conversational assistant.

        You MUST use the conversation history when answering.

        If the user's name, preferences, or facts are mentioned in the conversation history, use them.

        Conversation History:
        {history_text}

        Current User Message:
        {message}

        Answer the current user message using the conversation history.
        """

        memory_response = MemoryExtractorService.extract_memory(
            message
        )
        print("\nMEMORY EXTRACTOR")
        print(memory_response)

        if memory_response.startswith("STORE:"):
            memory_text = (
                memory_response.replace("STORE:", "").strip()
            )

            MemoryService.save_memory(
                memory_id=str(uuid4()),
                memory_text=memory_text,
            )

            print(
                "MEMORY SAVED"
            )

        response = (
            RAGService.answer_question(
                question=message,
                chat_history=chat_history
            )
        )

        return response["answer"]
