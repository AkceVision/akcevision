from pydantic import BaseModel


class NewsItem(BaseModel):
    """
    Standard news model used inside AkceVision.
    """

    title: str
    description: str | None = None
    url: str
    image_url: str | None = None
    source: str
    published_at: str

class NewsResponse(BaseModel):
    """
    Standard API response for news.
    """

    status: str
    count: int
    data: list[NewsItem]