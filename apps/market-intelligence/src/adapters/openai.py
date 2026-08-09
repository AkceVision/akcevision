from openai import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

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

        try:

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

        except RateLimitError:
            return (
                "OpenAI API quota exceeded. "
                "Please check your API billing or remaining credits."
            )

        except AuthenticationError:
            return (
                "OpenAI authentication failed. "
                "Please verify your API key."
            )

        except APITimeoutError:
            return (
                "OpenAI request timed out."
            )

        except APIConnectionError:
            return (
                "Unable to connect to OpenAI."
            )

        except Exception as exc:
            return f"OpenAI Error: {exc}"