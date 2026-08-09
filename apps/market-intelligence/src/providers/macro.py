from src.adapters.fred import FredAdapter


class MacroProvider:
    """
    Macro Provider.
    """

    def __init__(self):
        self.adapter = FredAdapter()

    def get_indicator(
        self,
        indicator: str,
    ):
        """
        Get macroeconomic indicator.
        """
        return self.adapter.get_indicator(indicator)

    def health_check(self):
        """
        Macro provider health.
        """
        return {
            "provider": self.adapter.__class__.__name__,
            "configured": True,
        }