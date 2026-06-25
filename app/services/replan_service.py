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

The previous plan did not gather enough
information to answer the question.

Create a better execution plan.

Available Steps:

- Search Memory
- Search PDF
- Generate Answer

Return ONLY the numbered plan.
"""

        return GeminiService.generate(
            prompt
        )