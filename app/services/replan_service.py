from app.services.gemini_service import GeminiService


class ReplanService:

    @staticmethod
    def create_replan(
            question: str,
            observation: list[str]
    ):

        observation_text = "\n".join(
            observation
        )

        prompt = f"""
        You are an AI replanner.

        Question:
        {question}

        Current Observation:
        {observation_text}

        The previous execution plan did not gather
        enough information.

        Create a new execution plan.

        Available Steps:

        - Search Memory
        - Search PDF
        - Generate Answer

        Rules:

        1. Use ONLY the exact step names listed above.

        2. Do NOT modify the step names.

        3. Do NOT add explanations.

        4. Do NOT add descriptions after a step.

        5. Return ONLY the numbered plan.

        Examples:

        1. Search Memory
        2. Generate Answer

        or

        1. Search PDF
        2. Generate Answer

        or

        1. Search Memory
        2. Search PDF
        3. Generate Answer
        """

        return GeminiService.generate(
            prompt
        )