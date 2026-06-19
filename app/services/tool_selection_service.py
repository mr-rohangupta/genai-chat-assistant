from app.services.gemini_service import GeminiService

class ToolSelectionService:

    @staticmethod
    def select_tool(
            question: str
    ):
        prompt = f"""
    You are a tool selection agent.

    Available Tools:

    1. memory
       - User preferences
       - User facts
       - Personal information

    2. pdf
       - Uploaded PDF data
       - Quotation information
       - Document information

    Question:
    {question}

    Return ONLY:

    memory

    OR

    pdf
    """

        response = (
            GeminiService.generate(prompt)
        )

        return response.strip().lower()