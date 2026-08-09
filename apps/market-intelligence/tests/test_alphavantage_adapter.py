from src.adapters.alphavantage import AlphaVantageAdapter
from src.models.market import MarketQuote


def test_map_quote():
    """
    Alpha Vantage response should be converted to MarketQuote.
    """

    adapter = AlphaVantageAdapter()

    response = {
        "Global Quote": {
            "01. symbol": "AAPL",
            "05. price": "231.25",
            "09. change": "-1.21",
            "10. change percent": "-0.52%",
        }
    }

    quote = adapter.map_quote(response)

    assert isinstance(quote, MarketQuote)
    assert quote.symbol == "AAPL"
    assert quote.price == 231.25
    assert quote.change == -1.21
    assert quote.change_percent == -0.52