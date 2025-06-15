# This file defines the ToolAgent that solves tasks using registered tools

from tools.tool_registry import tool_selector

# Given a task, select and apply the appropriate tool to solve it.

def solve_task(task):
    tool = tool_selector(task)
    return tool.run(task)