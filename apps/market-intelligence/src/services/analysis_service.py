from src.services.ai_service import AIService
from src.services.crypto_service import CryptoService
from src.services.macro_service import MacroService
from src.services.market_service import MarketService
from src.services.news_service import NewsService


class AnalysisService:
    """
    AI-powered market analysis service.
    """

    def __init__(self):
        self.market_service = MarketService()
        self.news_service = NewsService()
        self.crypto_service = CryptoService()
        self.macro_service = MacroService()
        self.ai_service = AIService()

    def analyze(
        self,
        symbol: str = "AAPL",
    ):
        """
        Collect data from all intelligence providers
        and request an AI-generated analysis.
        """

        market = self.market_service.get_quote(symbol)

        macro = self.macro_service.get_indicator("FEDFUNDS")

        crypto = self.crypto_service.get_quote("bitcoin")

        news = self.news_service.get_latest()

        system_prompt = (
            "You are a senior financial analyst. "
            "Analyze the supplied financial data and return "
            "a concise professional market summary."
        )

        user_prompt = f"""
Market
------
{market}

Macro
-----
{macro}

Crypto
------
{crypto}

News
----
{news}
"""

        summary = self.ai_service.ask(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "symbol": symbol,
            "market": market,
            "macro": macro,
            "crypto": crypto,
            "news_count": len(news),
            "analysis": summary,
        }

    def health_check(self):
        """
        Analysis service health.
        """
        return self.ai_service.health_check()