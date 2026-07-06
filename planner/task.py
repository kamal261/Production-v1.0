from dataclasses import dataclass


@dataclass
class Task:

    tool: str

    input: dict

    priority: int = 1