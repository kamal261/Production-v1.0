class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, name):

        return self.tools.get(name)

    def run(self, name, *args, **kwargs):

        tool = self.get(name)

        if not tool:
            raise ValueError(f"Tool not found: {name}")

        return tool.run(*args, **kwargs)