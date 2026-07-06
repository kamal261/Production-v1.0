from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ApplicationState:

    project_name: str

    mode: str

    loaded_modules: Dict[str, Any] = field(default_factory=dict)

    runtime: Dict[str, Any] = field(default_factory=dict)

    statistics: Dict[str, Any] = field(default_factory=dict)