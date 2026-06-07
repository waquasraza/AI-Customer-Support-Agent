from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retriever import get_relevant_documents
from app.services.support_agent import generate_support_answer
from app.services.agents.router_agent import route_question
from app.services.agents.billing_agent import handle_billing_query
from app.services.agents.technical_agent import handle_technical_query
from app.services.agents.account_agent import handle_account_query
from app.services.escalation_agent import escalate_issue
from app.services.memory_service import get_memory
from app.services.conversation_service import (
    save_message,
    get_conversation_history
)

router = APIRouter(
    prefix="/chat",
    tags=["Support Chat"]
)


class ChatRequest(BaseModel):
    session_id: str
    question: str


@router.post("/")
async def chat(request: ChatRequest):

    agent_type = route_question(
    request.question
    )

    history_text = get_conversation_history(request.session_id)
    
    print("\n===== CHAT HISTORY =====")
    print(history_text)
    print("========================\n")

    if agent_type == "billing":

        answer = handle_billing_query(
            request.question,
            history_text
        )

    elif agent_type == "technical":

        answer = handle_technical_query(
            request.question,
            history_text
        )

    elif agent_type == "account":

        answer = handle_account_query(
            request.question,
            history_text
        )

    else:

        docs = get_relevant_documents(
            request.question,
            history_text
        )

        answer = generate_support_answer(
            request.question,
            docs,
            history_text
        )

    if ("could not find" in answer.lower()):

        save_message(
            request.session_id,
            "user",
            request.question
        )

        save_message(
            request.session_id,
            "assistant",
            answer
        )
        
        ticket = escalate_issue(
            request.question,
            agent_type
        )

        return {
            "agent": agent_type,
            "escalated": True,
            "ticket": ticket,
            "message": "Support ticket created."
        }
    
    save_message(
        request.session_id,
        "user",
        request.question
    )

    save_message(
        request.session_id,
        "assistant",
        answer
    )
    
    return {
    "agent": agent_type,
    "question": request.question,
    "answer": answer
    }