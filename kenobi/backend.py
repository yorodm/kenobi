# coding: utf-8
from jedi import Script
from jedi.api.classes import Completion, Definition
from kenobi.util import uri_to_path
from typing import List


def complete(uri: str, content: str, line: int, char: int) -> List[Completion]:
    path = uri_to_path(uri)
    return Script(content, line, char, path).completions()


def find_definition(uri, content, line, char) -> List[Definition]:
    path = uri_to_path(uri)
    return Script(content, line, char, path).goto_definitions()
