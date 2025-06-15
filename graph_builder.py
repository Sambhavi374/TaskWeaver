# Constructs the LangGraph state graph for the agent system.

from langgraph.graph import StateGraph
from agents.plan_agent import plan_query
from agents.tool_agent import solve_task
from state import AgentState

def plan_node(state):
    state.tasks = plan_query(state.query)
    return state

def solve_node(state):
    if not state.tasks:
        return state
    task = state.tasks.pop(0)
    state.current_task = task
    result = solve_task(task)
    state.results.append((task, result))
    return state

def build_graph():
    graph = StateGraph()
    graph.add_node("planner", plan_node)
    graph.add_node("solver", solve_node)
    graph.set_entry_point("planner")
    graph.add_edge("planner", "solver")
    graph.add_edge("solver", "solver")
    return graph
