# This file registers available tools and defines logic for selecting them

from langchain.agents import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

# tools
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
duckduckgo = DuckDuckGoSearchRun()
weather = WeatherTool()
task_manager = TaskManagerTool()

# List of available tools
TOOLS = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Useful for factual lookups and summaries."
    ),

    Tool(
        name="DuckDuckGoSearch", 
        func=duckduckgo.run, 
        description="Useful for general web search queries."
    ),

    Tool(
        name="Weather", 
        func=weather.run, 
        description="Provides weather updates for a given location (simulated)."
    ),

    Tool(
        name="TaskManager", 
        func=task_manager.run, 
        description="Manages personal task lists and to-dos (simulated)."
    )
]


# Select appropriate tool based on task content

def tool_selector(task):
    task_lower = task.lower()
    if any(keyword in task_lower for keyword in ["who", "what is", "define"]):
        return TOOLS[0]  # Wikipedia

    elif any(keyword in task_lower for keyword in ["search", "find", "latest"]):
        return TOOLS[1]  # DuckDuckGoSearch

    elif any(keyword in task_lower for keyword in ["weather", "temperature", "forecast"]):
        return TOOLS[2]  # Weather

    elif any(keyword in task_lower for keyword in ["remind", "task", "to-do", "list"]):
        return TOOLS[3]  # Task Manager
        
    return TOOLS[1]  # Default to DuckDuckGoSearch