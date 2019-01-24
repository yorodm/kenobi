# coding: utf-8
from pygls.server import LanguageServer


class PythonLanguageServer(LanguageServer):

    def __init__(self) -> None:
        super().__init__()


__py_server = PythonLanguageServer()

feature = __py_server.feature
command = __py_server.command
