from app.services.agents.account_agent import handle_account_query

def account_node(state):

    state["answer"] = handle_account_query(
        state["question"],
        state["history_text"]
    )

    return state