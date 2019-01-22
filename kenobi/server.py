# coding: utf-8
from typings import Any, List
from pygls.server import LanguageServer


class PythonLanguageServer(LanguageServer):

    def __init__(self) -> None:
        super().__init__()


server = PythonLanguageServer()
