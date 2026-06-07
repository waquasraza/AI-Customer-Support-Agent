from typing import TypedDict


class SupportState(TypedDict):

    session_id: str

    question: str

    history_text: str

    agent_type: str
    
    answer: str

    escalated: bool
    
    ticket: dict | None