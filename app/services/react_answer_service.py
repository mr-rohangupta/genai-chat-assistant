from app.services.gemini_service import GeminiService

class ReActAnswerService:

    @staticmethod
    def generate_answer(
            question: str,
            observation: list[str]
    ):

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

Provide a clear and concise answer.
"""

        response = (
            GeminiService.generate(
                prompt
            )
        )

        return response