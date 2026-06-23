from pathlib import Path
import chromadb

from app.core.logger import get_logger

logger = get_logger(__name__)
BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

DB_PATH = BASE_DIR / "chroma_db"

class VectorDBService:

    client = chromadb.PersistentClient(
        path=str(DB_PATH)
    )

    memory_collection = (
        client.get_or_create_collection(
            name="memory_collection"
        )
    )

    pdf_collection = (
        client.get_or_create_collection(
            name="pdf_collection"
        )
    )

    @staticmethod
    def search_documents(
            query: str,
            top_k: int = 5
    ):

        results = VectorDBService.pdf_collection.query(
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

        VectorDBService.pdf_collection.add(
            documents=chunks,
            ids=ids
        )

        logger.info(
            f"{len(chunks)} chunks stored in ChromaDB"
        )