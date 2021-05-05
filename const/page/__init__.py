from typing import NamedTuple, List
import yaml


class Element(NamedTuple):
    name: str
    description: str
    type: str
    selector: str


class Page(NamedTuple):
    name: str
    description: str
    url: str
    elements: List[Element]


with open('pages.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

page_setting = {}
for race_type, pages in config.items():
    for page_key, page in pages.items():
        elements = page.get('elements')
        page_setting[race_type][page_key] = Page(
            page.get('name'),
            page.get('description'),
            page.get('url'),
            [Element(
                element.get('name'),
                element.get('description'),
                element.get('type'),
                element.get('selector'),
            ) for element in elements],
        )