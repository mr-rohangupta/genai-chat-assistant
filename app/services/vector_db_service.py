import chromadb

from app.core.logger import get_logger

logger = get_logger(__name__)

class VectorDBService:

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="chat_knowledge_base"
    )

    @staticmethod
    def search_documents(
            query: str,
            top_k: int = 5
    ):

        results = VectorDBService.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        return results

    @staticmethod
    def store_documents(
            chunks: list[str]
    ):
        ids = []

        for index, _ in enumerate(chunks):
            ids.append(
                f"pdf_chunk_{index}"
            )

        VectorDBService.collection.add(
            documents=chunks,
            ids=ids
        )

        logger.info(
            f"{len(chunks)} chunks stored in ChromaDB"
        )