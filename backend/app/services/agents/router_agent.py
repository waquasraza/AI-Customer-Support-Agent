from langchain_openai import ChatOpenAI

from app.core.config import OPENAI_API_KEY


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)

CATEGORY_MAP = {
    "pricing": "billing",
    "refunds": "billing",
    "payments": "billing",

    "technical": "technical",
    "api": "technical",
    "integration": "technical",
    "integrations": "technical",

    "account": "account",
    "authentication": "account",
    "login": "account"
}

def route_question(question: str):

    prompt = f"""
    You are a routing agent.

    Your job is to classify customer questions into ONE category.

    Available categories:

    billing
    - pricing
    - plans
    - refunds
    - invoices
    - subscriptions
    - payments

    technical
    - api
    - integrations
    - bugs
    - errors
    - technical issues

    account
    - login
    - password
    - account settings
    - profile
    - authentication

    Rules:
    - Return ONLY one word.
    - Do not explain.
    - Do not add punctuation.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    agent = CATEGORY_MAP.get(
    response.content.strip().lower(),
    "technical"
    )


    allowed_agents = [
        "billing",
        "technical",
        "account"
    ]

    if agent not in allowed_agents:
        return "technical"

    return agent