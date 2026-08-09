from src.providers.ai import AIProvider


class AIService:
    """
    AI Service.
    """

    def __init__(self):
        self.provider = AIProvider()

    def ask(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Send prompt to AI provider.
        """
        return self.provider.chat(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

    def health_check(self):
        """
        AI health.
        """
        return self.provider.health_check()