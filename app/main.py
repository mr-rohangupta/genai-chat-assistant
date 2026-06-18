from fastapi import FastAPI

from app.api.routes import router
from app.api import pdf_router

app = FastAPI(
    title="GenAI Chat Assistant"
)

app.include_router(
    router
)

app.include_router(
    pdf_router.router,
    tags=["PDF"]
)