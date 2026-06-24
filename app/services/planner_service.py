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

Available Tools:

- memory
- pdf

Planning Rules:

1. First determine the question type.

Question Types:

A. Memory Question
   - User facts
   - User preferences
   - User profile information
   - Stored memories

B. PDF Question
   - Uploaded documents
   - PDF content
   - Document summaries
   - Information contained in PDFs

C. Hybrid Question
   - Requires both Memory and PDF data

2. Create the plan based on the question type.

3. Always finish with:
   Generate Answer

Allowed Steps:

- Search Memory
- Search PDF
- Generate Answer

You MUST use ONLY the allowed steps.

Do not invent new steps.

Do not add explanations.

Return ONLY the numbered plan.

Examples:

Memory Question:
1. Search Memory
2. Generate Answer

PDF Question:
1. Search PDF
2. Generate Answer

Hybrid Question:
1. Search Memory
2. Search PDF
3. Generate Answer
"""

        return GeminiService.generate(
            prompt
        )