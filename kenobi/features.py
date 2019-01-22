# coding: utf-8
import sys
from pygls.features import (
    COMPLETION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_CLOSE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
)
from pygls.types import CompletionParams, CompletionList, CompletionItem
from kenobi.server import PythonLanguageServer, py_server
from kenobi.backend import complete, jedi_to_lsp_kind


@py_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def document_changed():
    pass


@py_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def document_closed():
    pass


@py_server.feature(TEXT_DOCUMENT_DID_OPEN)
def document_open():
    pass


@py_server.feature(TEXT_DOCUMENT_DID_SAVE)
def document_saved():
    pass


@py_server.feature(COMPLETION, trigger_character=["."])
def complete_code(ls, c: CompletionParams) -> CompletionList:  # noqa
    doc = ls.workspace.get_document(c.textDocument.uri)
    completions = complete(
        doc.uri, doc.source, c.position.line + 1, c.position.character
    )
    items = [
        CompletionItem(x.name, jedi_to_lsp_kind(x.type), documentation=x.docstring()) # noqa
        for x in completions
    ]
    return CompletionList(False, items)
