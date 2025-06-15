from graph_builder import build_graph
from state import AgentState

if __name__ == "__main__":
    user_input = input("Enter your query: ")
    state = AgentState(user_input)
    graph = build_graph()
    final_state = graph.execute(state)

    print("\nFinal Results:")
    for task, result in final_state.results:
        print(f"Task: {task}\nResult: {result}\n")