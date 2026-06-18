from pathlib import Path
from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from app.services.chunking_service import ChunkingService
from app.services.pdf_service import PdfService
from app.services.vector_db_service import VectorDBService

router = APIRouter()

UPLOAD_DIR = "uploads"

Path(
    UPLOAD_DIR
).mkdir(
    exist_ok=True
)

@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = Path(UPLOAD_DIR) / file.filename

    with open(file_path, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    text = PdfService.extract_text(
        str(file_path)
    )

    chunks = ChunkingService.split_text(
        text=text,
        chunk_size=200
    )

    VectorDBService.store_documents(
        chunks
    )

    return {
        "file_name": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "message": "PDF Uploaded Successfully"
    }

@router.get("/search-pdf")
async def search_pdf(
        query: str
):

    results = VectorDBService.search_documents(
        query=query,
        top_k=3
    )

    return results