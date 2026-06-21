from app.services.question_rewriter_service import QuestionRewriterService
from app.services.react_executor_service import ReActExecutorService


class RAGService:

    @staticmethod
    def answer_question(
            question: str,
            chat_history: list
    ):

        rewritten_question = (
            QuestionRewriterService.rewrite_question(question, chat_history)
        )

        print("\nREWRITTEN QUESTION")
        print(rewritten_question)

        react_result = (
            ReActExecutorService.execute(
                rewritten_question
            )
        )

        return {
            "rewritten_question": rewritten_question,
            "thought": react_result["thought"],
            "action": react_result["action"],
            "observation": react_result["observation"],
            "answer": react_result["answer"]
        }