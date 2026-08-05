import requests
from requests import Response


class HttpClient:
    """
    Shared HTTP client for external API integrations.
    """

    DEFAULT_TIMEOUT = 30

    def get(
        self,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> dict:

        response: Response = requests.get(
            url=url,
            params=params,
            headers=headers,
            timeout=self.DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return response.json()
