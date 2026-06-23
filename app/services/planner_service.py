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

Create a short execution plan.

Available tools:

- memory
- pdf

Return ONLY the plan.

Example:

1. Search Memory
2. Generate Answer
"""

        return GeminiService.generate(
            prompt
        )