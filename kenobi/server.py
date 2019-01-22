# coding: utf-8
from pygls.server import LanguageServer


class PythonLanguageServer(LanguageServer):

    def __init__(self) -> None:
        super().__init__()


py_server = PythonLanguageServer()
