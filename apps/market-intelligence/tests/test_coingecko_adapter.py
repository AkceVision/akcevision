from src.adapters.coingecko import CoinGeckoAdapter
from src.models.crypto import CryptoQuote


def test_map_quote():
    adapter = CoinGeckoAdapter()

    response = {
        "bitcoin": {
            "usd": 64929,
            "usd_market_cap": 1302987190671.19,
            "usd_24h_vol": 12364511914.70,
            "usd_24h_change": -0.051068,
        }
    }

    quote = adapter.map_quote(
        "bitcoin",
        response,
    )

    assert isinstance(quote, CryptoQuote)
    assert quote.symbol == "bitcoin"
    assert quote.price == 64929
    assert quote.market_cap == 1302987190671.19
    assert quote.volume_24h == 12364511914.70
    assert quote.change_percent_24h == -0.051068
    assert quote.currency == "USD"