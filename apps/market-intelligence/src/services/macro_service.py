from src.providers.macro import MacroProvider


class MacroService:
    """
    Macro Service.
    """

    def __init__(self):
        self.provider = MacroProvider()

    def get_indicator(
        self,
        indicator: str,
    ):
        """
        Get macroeconomic indicator.
        """
        return self.provider.get_indicator(indicator)

    def health_check(self):
        """
        Macro health check.
        """
        return self.provider.health_check()