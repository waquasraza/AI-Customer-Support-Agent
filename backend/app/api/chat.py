from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.support_graph import support_graph

router = APIRouter(prefix="/chat", tags=["Support Chat"])

class ChatRequest(BaseModel):
    session_id: str
    question: str


@router.post("/")
async def chat(request: ChatRequest):

    result = support_graph.invoke(
    {
        "session_id": request.session_id,
        "question": request.question,
        "history_text": "",
        "agent_type": "",
        "answer": "",
        "escalated": False,
        "ticket": None
    })

    if result["escalated"]:

        return {
            "agent": result["agent_type"],
            "escalated": True,
            "ticket": result["ticket"],
            "message": "Support ticket created."
        }

    return {
        "agent": result["agent_type"],
        "question": result["question"],
        "answer": result["answer"]
    }