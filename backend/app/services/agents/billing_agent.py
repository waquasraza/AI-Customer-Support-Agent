from app.services.retriever import get_relevant_documents
from app.services.support_agent import generate_support_answer


def handle_billing_query(
    question: str,
    history: str = ""
    ):

    docs = get_relevant_documents(question)

    answer = generate_support_answer(
        question,
        docs,
        history
    )

    return answer