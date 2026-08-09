from src.adapters.openai import OpenAIAdapter


class AIProvider:
    """
    AI Provider.
    """

    def __init__(self):
        self.adapter = OpenAIAdapter()

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Send prompt to AI.
        """
        return self.adapter.chat(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

    def health_check(self):
        """
        AI provider health.
        """
        return {
            "provider": self.adapter.__class__.__name__,
            "configured": True,
        }