from src.providers.crypto import CryptoProvider


class CryptoService:
    """
    Crypto Service.
    """

    def __init__(self):
        self.provider = CryptoProvider()

    def get_quote(
        self,
        symbol: str,
    ):
        """
        Get crypto quote.
        """
        return self.provider.get_quote(symbol)

    def health_check(self):
        """
        Crypto health check.
        """
        return self.provider.health_check()