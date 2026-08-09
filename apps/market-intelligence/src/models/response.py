from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    """
    Standard API response model.
    """

    status: str
    count: int
    data: list[Any]