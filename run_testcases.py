from app.services.testcase_service import TestCaseService

service = TestCaseService()

service.generate_for_modified_sections(
    old_version=1,
    new_version=2
)