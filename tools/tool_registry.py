# This file registers available tools and defines logic for selecting them

from langchain.agents import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper



# tools
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


# List of available tools
TOOLS = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Useful for factual lookups and summaries."
    )
]


# Select appropriate tool based on task content

def tool_selector(task):
    return TOOLS[0]