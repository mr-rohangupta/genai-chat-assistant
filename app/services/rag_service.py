from app.services.gemini_service import GeminiService
from app.services.question_rewriter_service import QuestionRewriterService
from app.tools.tool_router import ToolRouter

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

        documents = ToolRouter.route(
            rewritten_question
        )

        knowledge_context = "\n".join(
            documents
        )

        print("\nRETRIEVED DOCUMENTS")

        for doc in documents:
            print(doc)

        context = f"""
                CONTEXT:
                {knowledge_context}
                """

        prompt = f"""
     You are a helpful AI assistant.

    Answer the question using ONLY the context below.

    Context:

    {context}

    Question:

    {rewritten_question}

    Answer:
    """

        print("\nFINAL PROMPT")
        print(prompt)

        response = (
            GeminiService.generate(prompt)
        )

        return {
            "rewritten_question": rewritten_question,
            "retrieved_documents": documents,
            "answer": response
        }



