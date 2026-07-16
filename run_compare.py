from app.services.comparison_service import ComparisonService

service = ComparisonService()

result = service.compare(
    version1=1,
    version2=2
)

print("\nAdded Sections")
print(result["added"])

print("\nDeleted Sections")
print(result["deleted"])

print("\nModified Sections")
print(result["modified"])

print("\nUnchanged Sections")
print(result["unchanged"])