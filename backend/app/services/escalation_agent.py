from app.services.ticket_service import create_ticket


def escalate_issue( question: str, category: str):
    
    return create_ticket(
        question,
        category
    )