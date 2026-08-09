from src.adapters.finnhub import FinnhubAdapter
from src.models.market import MarketQuote


def test_map_quote():
    """
    Finnhub response should be converted to MarketQuote.
    """

    adapter = FinnhubAdapter()

    response = {
        "c": 313.33,
        "d": 0.92,
        "dp": 0.2945,
    }

    quote = adapter.map_quote(
        "AAPL",
        response,
    )

    assert isinstance(quote, MarketQuote)
    assert quote.symbol == "AAPL"
    assert quote.price == 313.33
    assert quote.change == 0.92
    assert quote.change_percent == 0.2945