from langchain_openai import ChatOpenAI

from app.core.config import OPENAI_API_KEY


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)

def route_question(question: str):

    prompt = f"""
    You are a routing agent.

    Classify the customer question into exactly one category.

    Categories:
    - billing
    - technical
    - account

    Return ONLY one word.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    agent = response.content.strip().lower()

    if agent not in ["billing", "technical", "account"]:
        return "technical"

    return agent