from app.services.agents.technical_agent import handle_technical_query

def technical_node(state):

    state["answer"] = handle_technical_query(
        state["question"],
        state["history_text"]
    )

    return state