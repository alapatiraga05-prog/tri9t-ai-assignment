from fastapi import APIRouter

from app.services.testcase_service import TestCaseService
from app.services.mongodb_service import MongoDBService

router = APIRouter(
    prefix="/testcases",
    tags=["testcases"]
)


@router.post("/generate/{old_version}/{new_version}")
def generate_testcases(
    old_version: int,
    new_version: int
):

    service = TestCaseService()

    service.generate_for_modified_sections(
        old_version,
        new_version
    )

    return {
        "message": "Test cases generated successfully."
    }


@router.get("/{version}")
def get_testcases(
    version: int
):

    mongo = MongoDBService()

    data = mongo.get_testcases(version)

    return {
        "version": version,
        "count": len(data),
        "test_cases": data
    }