from app.services.gemini_service import GeminiService

class ReActAgentService:

    @staticmethod
    def think(
            question: str
    ):

        prompt = f"""
You are a ReAct Agent.

Available Tools:

1. memory
   - User preferences
   - User facts
   - User information

2. pdf
   - Uploaded PDF information
   - Quotations
   - Documents

Question:
{question}

Think step-by-step.

Return ONLY:

THOUGHT: <your reasoning>

ACTION: memory

OR

ACTION: pdf
"""

        response = (
            GeminiService.generate(
                prompt
            )
        )

        return response