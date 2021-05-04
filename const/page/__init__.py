from typing import NamedTuple, Type, List


class Element(NamedTuple):
    name: str
    description: str
    type: str
    selector: str


class Page(NamedTuple):
    name: str
    description: str
    url: str
    elements: List[Type[Element]]
