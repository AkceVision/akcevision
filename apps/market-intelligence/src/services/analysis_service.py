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
        self.news = NewsService()
        self.market = MarketService()
        self.crypto = CryptoService()
        self.macro = MacroService()
        self.ai = AIService()

    def analyze(
        self,
        symbol: str = "AAPL",
    ):
        """
        Analyze market data using AI.
        """

        market = self.market.get_quote(symbol)

        macro = self.macro.get_indicator("FEDFUNDS")

        crypto = self.crypto.get_quote("bitcoin")

        news = self.news.get_latest()

        system_prompt = (
            "You are an expert financial market analyst. "
            "Analyze the supplied market information and "
            "return a concise professional summary."
        )

        user_prompt = f"""
Market:
{market}

Macro:
{macro}

Crypto:
{crypto}

News:
{news}
"""

        summary = self.ai.ask(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return {
            "symbol": symbol,
            "market": market,
            "macro": macro,
            "crypto": crypto,
            "news_count": len(news),
            "summary": summary,
        }