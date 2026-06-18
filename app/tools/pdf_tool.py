from app.services.vector_db_service import VectorDBService

class PdfTool:

    @staticmethod
    def execute(
            query: str
    ):

        results = (
            VectorDBService.search_documents(
                query=query,
                top_k=5
            )
        )

        documents = (
            results["documents"][0]
            if results["documents"]
            else []
        )

        return documents