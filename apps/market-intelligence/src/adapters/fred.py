from src.adapters.base import BaseAdapter
from src.config import settings
from src.models.macro import MacroIndicator


class FredAdapter(BaseAdapter):
    """
    Adapter for FRED.
    """

    BASE_URL = settings.FRED_URL

    def get_indicator(
        self,
        indicator: str,
    ) -> MacroIndicator:
        """
        Get latest macroeconomic indicator.
        """

        response = self.client.get(
            self.BASE_URL,
            params={
                "series_id": indicator,
                "api_key": settings.FRED_API_KEY,
                "file_type": "json",
                "sort_order": "desc",
                "limit": 1,
            },
        )

        return self.map_indicator(
            indicator,
            response,
        )

    def map_indicator(
        self,
        indicator: str,
        response: dict,
    ) -> MacroIndicator:
        """
        Convert FRED response into MacroIndicator.
        """

        observations = response.get("observations", [])

        if not observations:
            return MacroIndicator(
                indicator=indicator,
                value=0.0,
                unit=None,
                country="US",
                date=None,
            )

        latest = observations[0]

        value = latest.get("value", "0")

        try:
            value = float(value)
        except ValueError:
            value = 0.0

        return MacroIndicator(
            indicator=indicator,
            value=value,
            unit="Percent",
            country="US",
            date=latest.get("date"),
        )