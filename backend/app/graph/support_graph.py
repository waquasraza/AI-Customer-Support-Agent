from langgraph.graph import ( StateGraph, END )

from app.graph.state import SupportState 
from app.graph.nodes.router_node import router_node 
from app.graph.nodes.billing_node import billing_node 
from app.graph.nodes.technical_node import technical_node
from app.graph.nodes.account_node import account_node
from app.graph.nodes.escalation_node import escalation_node
from app.graph.nodes.load_memory_node import load_memory_node
from app.graph.nodes.save_memory_node import save_memory_node


def route_by_agent(state):

    return state["agent_type"]


graph = StateGraph(SupportState )

graph.add_node( "router", router_node )

graph.add_node( "billing", billing_node )

graph.add_node( "technical", technical_node )

graph.add_node( "account", account_node )

graph.add_node( "escalation", escalation_node )

graph.add_node( "load_memory", load_memory_node )

graph.add_node( "save_memory", save_memory_node )

graph.set_entry_point( "load_memory")

graph.add_edge( "load_memory", "router" )

graph.add_conditional_edges("router", route_by_agent, {
        "billing": "billing",
        "technical": "technical",
        "account": "account"
    }
)

graph.add_edge( "billing", "escalation" )

graph.add_edge( "technical", "escalation" )

graph.add_edge( "account", "escalation" )

graph.add_edge( "escalation", "save_memory" )

graph.add_edge( "save_memory", END )

support_graph = graph.compile()