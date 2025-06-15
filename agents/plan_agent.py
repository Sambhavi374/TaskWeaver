# Responsible for planning the tasks from the user query

from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key = os.getenv("GOOGLE_API_KEY"))

# Prompt to break down query into sub-queries or tasks
PLAN_PROMPT = PromptTemplate.from_template(
    """
    You are a personal task planner of the user. 
    You are given a complex user query, you have to break it into a list of clear,simple and atomic sub-tasks.
    Each sub-task should be a single actoin that cannot be broken down any futher.

    Example: 
    Query: "I want to plan a trip to New Delhi for 3 days.
    Show me the best places to visit, during day and night .
    Also show me places to stay."
    Sub-tasks:
    1. Find the best places to visit in New Delhi during the day.
    2. Find the best places to visit in New Delhi during the night.
    3. Find the best places to stay in New Delhi.

    Query: {query}
    Sub-tasks:
    """
)


# Function to generate subtasks from query
def plan_query(query):
    prompt = PLAN_PROMPT.format(query=query)
    response = llm.predict(prompt)
    return [task.strip("- ") for task in response.strip().split("\n") if task.strip()]