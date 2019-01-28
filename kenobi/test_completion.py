# coding: utf-8

from unittest import TestCase
from unittest.mock import Mock
from pygls.workspace import Document, Workspace
from pygls.types import (
    CompletionParams,
    TextDocumentIdentifier,
    TextDocumentPositionParams,
    Position,
    CompletionContext,
    CompletionTriggerKind,
)

from kenobi.completion import complete_code, jump_to_definition, document_hover
from kenobi.util import uri_to_path

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
            Position(4, 13),
            CompletionContext(CompletionTriggerKind()),
        )
        completions = complete_code(server, params)
        self.assertTrue(
            any(filter(lambda x: x.label == "__doc__", completions.items))
        )

    def test_goto_definition_finds_file(self):
        server.workspace.get_document = Mock(return_value=fake_document)
        params = TextDocumentPositionParams(
            TextDocumentIdentifier(fake_document_uri),
            Position(1, 21)
        )
        definition = jump_to_definition(server, params)[0]
        self.assertTrue(
            uri_to_path(definition.uri).endswith('case.py')
        )

    def test_goto_definition_finds_line(self):
        server.workspace.get_document = Mock(return_value=fake_document)
        params = TextDocumentPositionParams(
            TextDocumentIdentifier(fake_document_uri),
            Position(1, 21)
        )
        definition = jump_to_definition(server, params)[0]
        start = definition.range.start
        self.assertTrue(
            start.line == 350 and start.character == 6
        )

    def test_hover(self):
        server.workspace.get_document = Mock(return_value=fake_document)
        params = TextDocumentPositionParams(
            TextDocumentIdentifier(fake_document_uri),
            Position(1, 21)
        )
        hover = document_hover(server, params)
        self.assertTrue(
            'A class whose instances are single test cases' in hover.value
        )
