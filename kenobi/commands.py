# coding: utf-8
from pygls.features import CODE_ACTION
from pygls.types import CodeActionParams, Command, CodeAction
from kenobi.server import command, feature
from typing import List, Union

CodeActions = Union(Union(List[Command], List[CodeAction]), None)

@feature(CODE_ACTION)
def calculate_code_actions(ls, params: CodeActionParams) -> CodeActions:
    pass
