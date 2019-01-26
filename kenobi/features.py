# coding: utf-8
from pygls.features import (
    COMPLETION,
    DEFINITION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_CLOSE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
)

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
