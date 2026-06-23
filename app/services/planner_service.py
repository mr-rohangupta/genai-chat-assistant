from app.services.gemini_service import GeminiService


class PlannerService:

    @staticmethod
    def create_plan(
            question: str
    ):
        prompt = f"""
        You are an AI planner.

        Question:
        {question}

        Your responsibility is to create an execution plan
        for answering the user's question.

        Available tools:

        - memory
        - pdf

        Planning Rules:

        1. Use Search Memory for personal facts,
           preferences, profile information,
           and stored memories.

        2. Use Search PDF for document-based
           questions.

        3. Use both tools if both sources
           may contain useful information.

        4. Always finish with:
           Generate Answer

        Return ONLY the plan.

        Example:

        1. Search Memory
        2. Generate Answer
        """

        return GeminiService.generate(
            prompt
        )