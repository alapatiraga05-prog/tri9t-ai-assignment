from app.services.ai_service import AIService

service = AIService()

result = service.generate_testcases(
    heading="4.2 Error Codes",
    body="""
The device displays E1 when the cuff is disconnected.
The device displays E2 when motion is detected.
The device displays E3 for sensor failure.
"""
)

print(result)