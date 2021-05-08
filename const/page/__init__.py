import os
import yaml


with open(f'{os.path.dirname(__file__)}/pages.yaml', 'r') as yml:
    page_config = yaml.safe_load(yml)