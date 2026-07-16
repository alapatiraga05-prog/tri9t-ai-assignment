from app.models.document import Document
from app.models.node import Node
from app.services.comparison_service import ComparisonService


def test_compare_documents_reports_added_changed_and_removed_nodes():
    left_document = Document(name="manual", version=1)
    left_document.nodes = [Node(heading="Intro", level=1, body="old body")]

    right_document = Document(name="manual", version=2)
    right_document.nodes = [
        Node(heading="Intro", level=1, body="new body"),
        Node(heading="Safety", level=1, body="new section"),
    ]

    result = ComparisonService().compare_documents(left_document, right_document)

    assert result["changed"][0]["heading"] == "Intro"
    assert result["added"][0]["heading"] == "Safety"
    assert result["removed"] == []
