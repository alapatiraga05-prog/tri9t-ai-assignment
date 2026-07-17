from app.services.comparison_service import ComparisonService


def test_compare_same_version():

    service = ComparisonService()

    result = service.compare(1, 1)

    assert result["added"] == []
    assert result["deleted"] == []
    assert result["modified"] == []