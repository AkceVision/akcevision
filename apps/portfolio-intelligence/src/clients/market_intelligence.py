import httpx


class MarketIntelligenceClient:
    def __init__(
        self,
        base_url: str = "http://localhost:8000",
    ):
        self.base_url = base_url.rstrip("/")

    def get_quote(self, symbol: str) -> dict:
        response = httpx.get(
            f"{self.base_url}/market",
            params={"symbol": symbol},
            timeout=10.0,
        )

        response.raise_for_status()

        return response.json()
