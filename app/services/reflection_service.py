from app.services.gemini_service import GeminiService

class ReflectionService:

    @staticmethod
    def evaluate(
            question: str,
            observation: list
    ):
        prompt = f"""
        You are an AI evaluator.

        Question:
        {question}

        Observation:
        {observation}

        Evaluate whether ALL information required to answer
        the question is present in the observation.

        Rules:

        1. If every part of the question can be answered from the observation,
           return ENOUGH.

        2. If any part of the question is missing,
           return NEED_MORE_INFORMATION.

        3. Do not guess.

        Return ONLY one of:

        ENOUGH

        NEED_MORE_INFORMATION
        """

        response = (
            GeminiService.generate(
                prompt
            )
        )

        return response.strip()