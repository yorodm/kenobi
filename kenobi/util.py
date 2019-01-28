import os
import pathlib
from urllib import parse
from pygls.types import CompletionItemKind
from kenobi.server import command

IS_WIN = os.name == "nt"


TYPES = {
    "module": CompletionItemKind.Module,
    "class": CompletionItemKind.Class,
    "instance": CompletionItemKind.Reference,
    "function": CompletionItemKind.Function,
}


def uri_to_path(uri: str) -> str:
    parse_info = parse.urlparse(parse.unquote(uri))
    if IS_WIN:
        if parse_info.path.startswith("/"):
            return parse_info.path[1:]
    return parse_info.path


def path_to_uri(path: str) -> str:
    return pathlib.Path(path).as_uri()


def jedi_to_lsp_kind(jedi_kind: str) -> int:
    return TYPES.get(jedi_kind, CompletionItemKind.Text)
