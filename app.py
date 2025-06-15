import streamlit as st
from graph_builder import build_graph
from state import AgentState

st.set_page_config(page_title="Agentic Workflow", layout="wide")
st.title("🧠 LangGraph Agentic Workflow")
st.markdown("""
<style>
    .stApp { background-color: #f4f4f4; }
    .css-1cpxqw2 { font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

user_input = st.text_area("Enter your query:", placeholder="e.g., Plan a 3-day trip to Goa with food recommendations")

if st.button("Run Workflow"):
    if user_input.strip():
        state = AgentState(user_input)
        graph = build_graph()
        final_state = graph.execute(state)

        st.success("✅ Task execution completed!")
        st.subheader("Results")
        for task, result in final_state.results:
            st.markdown(f"**📝 Task:** {task}")
            st.markdown(f"**📄 Result:** {result}")
            st.markdown("---")
    else:
        st.warning("Please enter a query to proceed.")