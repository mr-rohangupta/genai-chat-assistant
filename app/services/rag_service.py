from app.services.question_rewriter_service import QuestionRewriterService
from app.services.planner_executor_service import PlannerExecutorService


class RAGService:

    @staticmethod
    def answer_question(
            question: str,
            chat_history: list
    ):
        """
        Main RAG orchestration service.

        Responsibilities
        ----------------
        1. Rewrite follow-up questions using chat history.
        2. Execute the Planner-Executor workflow.
        3. Return execution details and final answer.
        """

        rewritten_question = (
            QuestionRewriterService.rewrite_question(
                question,
                chat_history
            )
        )

        print("\nREWRITTEN QUESTION")
        print(rewritten_question)

        planner_result = (
            PlannerExecutorService.execute(
                rewritten_question
            )
        )

        return {
            "rewritten_question": rewritten_question,
            "plan": planner_result["plan"],
            "current_step": planner_result["current_step"],
            "completed_steps": planner_result["completed_steps"],
            "observation": planner_result["observation"],
            "reflection": planner_result["reflection"],
            "answer": planner_result["answer"]
        }