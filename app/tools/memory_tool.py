from app.services.memory_service import MemoryService

class MemoryTool:

    @staticmethod
    def execute(
            query: str
    ):

        results = (
            MemoryService.search_memories(
                query=query,
                top_k=3
            )
        )

        documents = (
            results["documents"][0]
            if results["documents"]
            else []
        )

        return documents