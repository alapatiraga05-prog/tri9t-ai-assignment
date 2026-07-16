from app.models.document import Document
from app.services.version_service import VersionService


def test_version_service_selects_latest_version():
    service = VersionService()
    docs = [Document(name="manual", version=1), Document(name="manual", version=3)]
    latest = service.get_latest_version(docs)
    assert latest.version == 3
