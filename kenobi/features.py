# coding: utf-8
import sys
from pygls.features import (
    COMPLETION,
    DEFINITION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_CLOSE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
)
from pygls.types import (
    CompletionParams,
    CompletionList,
    Location,
    TextDocumentPositionParams,
    CompletionItem,
    Range,
    Position,
)
from kenobi.server import feature
from kenobi.backend import complete, find_definition
from kenobi.util import jedi_to_lsp_kind, path_to_uri
from typing import List


@feature(TEXT_DOCUMENT_DID_CHANGE)
def document_changed():
    pass


@feature(TEXT_DOCUMENT_DID_CLOSE)
def document_closed():
    pass


@feature(TEXT_DOCUMENT_DID_OPEN)
def document_open():
    pass


@feature(TEXT_DOCUMENT_DID_SAVE)
def document_saved():
    pass


@feature(COMPLETION, trigger_character=["."])
def complete_code(ls, c: CompletionParams) -> CompletionList:  # noqa
    doc = ls.workspace.get_document(c.textDocument.uri)
    completions = complete(doc.uri, doc.source, c.position.line, c.position.character)
    items = [
        CompletionItem(
            x.name, jedi_to_lsp_kind(x.type), documentation=x.docstring()
        )
        for x in completions
    ]
    return CompletionList(False, items)


@feature(DEFINITION)
def jump_to_definition(ls, c: TextDocumentPositionParams) -> List[Location]:
    doc = ls.workspace.get_document(c.textDocument.uri)
    items = find_definition(
        doc.uri, doc.source, c.position.line + 1, c.position.character
    )
    return [
        Location(
            path_to_uri(item.module_path),
            Range(
                Position(item.line - 1, item.column),
                Position(item.line - 1, item.column + len(item.name)),
            ),
        )
        for item in items
    ]
