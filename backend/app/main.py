from fastapi import FastAPI

from app.core.init_db import init_db

from app.api.knowledge import router as knowledge_router
from app.api.chat import router as chat_router
from app.api.tickets import router as tickets_router

init_db()

app = FastAPI(
    title="AI Customer Support Agent"
)

app.include_router(knowledge_router)
app.include_router(chat_router)
app.include_router(tickets_router)


@app.get("/")
def health():
    return {
        "status": "running"
    }