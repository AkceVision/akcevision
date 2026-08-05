from src.clients.http_client import HttpClient


class BaseAdapter:
    """
    Base class for external API adapters.
    """

    def __init__(self):
        self.client = HttpClient()
