from pydantic import BaseModel


class MacroIndicator(BaseModel):
    """
    Standard macro economic indicator model.
    """

    indicator: str
    value: float
    unit: str | None = None
    country: str = "US"
    date: str | None = None