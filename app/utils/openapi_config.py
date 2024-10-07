import os
import toml

from functools import lru_cache
from pydantic import BaseModel

cwd = os.getcwd()
if cwd.endswith("tests"):
    toml_path = "../pyproject.toml"
else:
    toml_path = "pyproject.toml"


def get_version():
    return toml.load(toml_path)['tool']['poetry']['version']


def get_title():
    return toml.load(toml_path)['tool']['poetry']['name']


def get_authors():
    return {"authors": toml.load(toml_path)['tool']['poetry']['authors']}


def get_description():
    return toml.load(toml_path)['tool']['poetry']['description']


class Config(BaseModel):
    version: str = get_version()
    title: str = get_title()
    authors: dict = get_authors()
    description: str = get_description()


@lru_cache()
def get_config():
    return Config()


config = get_config()
