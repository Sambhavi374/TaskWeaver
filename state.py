# Defines the state object for tracking progress.

class AgentState:
    def __init__(self, query):
        self.query = query
        self.tasks = []
        self.results = []
        self.current_task = None