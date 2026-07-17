import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class AIService:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

        self.model = os.getenv("OPENROUTER_MODEL")

    def generate_testcases(self, heading, body):

        prompt = f"""
You are a Senior Software QA Engineer.

Generate ONLY 5 high-quality software test cases.

Section Heading:
{heading}

Section Content:
{body}

Generate:
1. Functional Test Cases
2. Negative Test Cases
3. Boundary Test Cases

Return ONLY valid JSON.

JSON Format:

{{
    "section": "{heading}",
    "test_cases": [
        {{
            "title": "",
            "type": "",
            "priority": "",
            "expected_result": ""
        }}
    ]
}}
"""

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.2,

                max_tokens=800
            )

            answer = response.choices[0].message.content.strip()

            # Remove markdown if present
            answer = answer.replace("```json", "")
            answer = answer.replace("```", "")
            answer = answer.strip()

            return json.loads(answer)

        except json.JSONDecodeError:

            print("\nAI Response:\n")
            print(answer)

            raise Exception("Model returned invalid JSON.")

        except Exception as e:

            raise Exception(f"OpenRouter Error: {e}")