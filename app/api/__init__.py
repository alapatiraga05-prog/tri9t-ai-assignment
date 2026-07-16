from app.api.document_api import router as document_router
from app.api.version_api import router as version_router
from app.api.testcase_api import router as testcase_router

__all__ = ["document_router", "version_router", "testcase_router"]
