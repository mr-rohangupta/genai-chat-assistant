from app.services.vector_db_service import VectorDBService

class MemoryService:

    @staticmethod
    def save_memory(
            memory_id: str,
            memory_text: str
    ):

        VectorDBService.collection.add(
            ids=[memory_id],
            documents=[memory_text],
            metadatas=[
                {
                    "type": "memory"
                }
            ]
        )

        return {
            "message": "Memory Stored Successfully",
        }

    @staticmethod
    def search_memories(
            query: str,
            top_k: int = 3
    ):

        results = (
            VectorDBService.collection.query(
                query_texts = [query],
                n_results=top_k,
                where={
                    "type": "memory"
                }
            )
        )

        return results