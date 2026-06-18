from app.services.gemini_service import (
    GeminiService
)


class QuestionRewriterService:

    @staticmethod
    def rewrite_question(
            question: str,
            chat_history: list
    ):

        if not chat_history:
            return question

        question_lower = question.lower()

        pronouns = [
            " he ",
            " she ",
            " they ",
            " it ",
            " him ",
            " her ",
            " that person ",
            " that candidate "
        ]

        if not any(
                pronoun in f" {question_lower} "
                for pronoun in pronouns
        ):
            return question

        history_text = ""

        for chat in chat_history:

            history_text += (
                f"{chat.role}: "
                f"{chat.content}\n"
            )

        prompt = f"""
You are a question rewriting assistant.

Your job is to rewrite ONLY follow-up questions
into standalone questions.

Rules:

1. If the input is already a complete standalone question,
return it unchanged.

2. If the input is a statement,
return it unchanged.

3. Only rewrite questions that contain references such as:

- he
- she
- they
- it
- him
- her
- that person
- that candidate

4. Never change the speaker's perspective.

Examples:

Input:
What is my name?

Output:
What is my name?

Input:
My favorite database is PostgreSQL

Output:
My favorite database is PostgreSQL

Input:
Tell me about Kafka

Output:
Tell me about Kafka

Conversation:

User:
Tell me about Rohan Gupta

Assistant:
Rohan Gupta is a Technical Architect.

Question:
How many years of experience does he have?

Output:
How many years of experience does Rohan Gupta have?

Conversation History:

{history_text}

Current Input:

{question}

Return ONLY the rewritten question.

Do not explain anything.
"""

        rewritten_question = (
            GeminiService.generate(
                prompt
            )
        )

        return rewritten_question.strip()