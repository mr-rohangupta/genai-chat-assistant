from app.services.gemini_service import GeminiService


class AnswerGenerationService:

    @staticmethod
    def generate_answer(
            question: str,
            observation: list[str]
    ):
        """
        Generates the final user-facing answer.

        Responsibilities
        ----------------
        1. Convert observations into context.
        2. Generate an answer using only
           the collected observations.
        3. Prevent unsupported information
           from being introduced.

        Inputs
        ------
        question:
            Original user question.

        observation:
            Tool outputs collected during
            Planner-Executor execution.

        Returns
        -------
        Final answer string.
        """

        observation_text = "\n".join(
            observation
        )

        prompt = f"""
You are a helpful AI assistant.

Question:
{question}

Observation:
{observation_text}

Answer the question using ONLY the observation.

Do not make assumptions.

Provide a clear and concise answer.
"""

        return GeminiService.generate(
            prompt
        )