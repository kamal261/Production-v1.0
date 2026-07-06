from dataclasses import dataclass, field
from typing import List


@dataclass
class Page:

    url: str
    html: str = ""

    title: str = ""
    status: int = 0

    links: List[str] = field(default_factory=list)
    headings: List[str] = field(default_factory=list)

    meta_description: str = ""
    canonical: str = ""

    visited: bool = False