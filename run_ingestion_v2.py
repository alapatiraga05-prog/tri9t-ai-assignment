from app.services.ingest_service import IngestService

service = IngestService()

service.ingest(
    pdf_path="data/ct200_manual_v2.pdf",
    document_name="CT200 Manual",
    version=2
)