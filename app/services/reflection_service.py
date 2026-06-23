from app.services.gemini_service import GeminiService


class ReflectionService:

    @staticmethod
    def evaluate(
            question: str,
            observation: list[str]
    ):
        """
        Evaluates whether the collected
        observations contain enough
        information to answer the question.

        Returns
        -------
        ENOUGH

        or

        NEED_MORE_INFORMATION
        """

        observation_text = "\n".join(
            observation
        )

        prompt = f"""
You are an AI evaluator.

Question:
{question}

Observation:
{observation_text}

Evaluate whether all information required
to answer the question exists in the observation.

Rules:

1. If every part of the question can be answered
   from the observation, return ENOUGH.

2. If any required information is missing,
   return NEED_MORE_INFORMATION.

3. Do not guess.

Return ONLY one of:

ENOUGH

NEED_MORE_INFORMATION
"""

        return (
            GeminiService.generate(
                prompt
            ).strip()
        )