from app.services.vector_db_service import VectorDBService

print(
    "\nMEMORY COUNT:"
)

print(
    VectorDBService.memory_collection.count()
)

print(
    "\nPDF COUNT:"
)

print(
    VectorDBService.pdf_collection.count()
)