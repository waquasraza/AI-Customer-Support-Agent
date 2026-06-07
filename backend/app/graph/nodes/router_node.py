from app.services.agents.router_agent import (
    route_question
)


def router_node(state):

    state["agent_type"] = route_question(
        state["question"]
    )

    return state