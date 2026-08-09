from openai import OpenAI

from src.config import settings


class OpenAIAdapter:
    """
    Adapter for OpenAI.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_BASE_URL,
        )

    @property
    def model(self):
        """
        Default AI model.
        """
        return settings.MODEL_NAME

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Send a chat completion request.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content