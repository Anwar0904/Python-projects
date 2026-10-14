from openai import OpenAI

from ai_chat_api.config import settings


class AIClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate_response(self, message: str) -> str:
        response = self.client.responses.create(
            model="gpt-5",
            input=message,
        )

        return response.output_text
