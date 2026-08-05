import requests


class HttpClient:
    """
    Shared HTTP client for external API integrations.
    """

    def get(self, url: str, params: dict | None = None, headers: dict | None = None):
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()
