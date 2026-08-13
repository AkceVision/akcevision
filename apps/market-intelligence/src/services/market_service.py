import time

from src.providers.market import MarketProvider


class MarketService:
    """
    Market Service.
    """

    CACHE_TTL_SECONDS = 60.0
    MIN_PROVIDER_INTERVAL_SECONDS = 1.1

    def __init__(self):
        self.provider = MarketProvider()
        self._quote_cache: dict[str, tuple[float, object]] = {}
        self._last_provider_request: float | None = None

    def get_quote(
        self,
        symbol: str,
    ):
        """
        Get market quote with in-memory caching and provider throttling.
        """

        normalized_symbol = symbol.strip().upper()

        if not normalized_symbol:
            raise ValueError("Symbol cannot be empty.")

        now = time.monotonic()

        cached = self._quote_cache.get(normalized_symbol)

        if cached is not None:
            cached_at, quote = cached

            if now - cached_at < self.CACHE_TTL_SECONDS:
                return quote

            del self._quote_cache[normalized_symbol]

        if self._last_provider_request is not None:
            elapsed = now - self._last_provider_request

            if elapsed < self.MIN_PROVIDER_INTERVAL_SECONDS:
                time.sleep(
                    self.MIN_PROVIDER_INTERVAL_SECONDS - elapsed
                )

        self._last_provider_request = time.monotonic()

        quote = self.provider.get_quote(normalized_symbol)

        self._quote_cache[normalized_symbol] = (
            time.monotonic(),
            quote,
        )

        return quote

    def health_check(self):
        """
        Market provider health check.
        """
        return self.provider.health_check()
