# coding: utf-8

from unittest import TestCase
from unittest.mock import Mock
from pygls.workspace import Document, Workspace
from pygls.types import (
    CompletionParams,
    TextDocumentIdentifier,
    Position,
    CompletionContext,
    CompletionTriggerKind,
)
from kenobi.features import complete_code

# Stolen from pygls sample server tests


class FakeServer:
    """We don't need real server to unit test features."""

    def __init__(self):
        self.workspace = Workspace("", None)


fake_document_uri = "file://fake_doc.txt"
fake_document_content = """
from unittest import TestCase

a = TestCase.
"""
fake_document = Document(fake_document_uri, fake_document_content)
server = FakeServer()
server.publish_diagnostics = Mock()
server.show_message = Mock()
server.show_message_log = Mock()


class TestServer(TestCase):
    def test_completion(self):
        fake_document_identifier = TextDocumentIdentifier(fake_document_uri)
        server.workspace.get_document = Mock(return_value=fake_document)
        params = CompletionParams(
            fake_document_identifier,
            Position(3, 13),
            CompletionContext(CompletionTriggerKind()),
        )
        completions = complete_code(server, params)
        self.assertTrue(
            any(filter(lambda x: x.label == "__doc__", completions.items))
        )
