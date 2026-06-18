from app.services.gemini_service import GeminiService
from app.services.question_rewriter_service import QuestionRewriterService
from app.services.vector_db_service import VectorDBService
from app.services.memory_service import MemoryService

class RAGService:

    @staticmethod
    def answer_question(
            question: str,
            chat_history: list
    ):

        rewritten_question = (
            QuestionRewriterService.rewrite_question(question, chat_history)
        )

        memory_results = MemoryService.search_memories(rewritten_question)

        memory_documents = (
            memory_results["documents"][0]
            if memory_results["documents"]
            else []
        )

        print("\nREWRITTEN QUESTION")
        print(rewritten_question)

        search_results = (
            VectorDBService.search_documents(rewritten_question)
        )

        documents = (
            search_results["documents"][0]
        )

        memory_context = "\n".join(memory_documents)

        knowledge_context = "\n".join(documents)

        print("\nRETRIEVED DOCUMENTS")

        for doc in documents:
            print(doc)

        context = f"""
        MEMORIES: 
        {memory_context}
        
        KNOWLEDGE: 
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



