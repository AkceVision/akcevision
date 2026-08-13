from fastapi import APIRouter, Depends, HTTPException

from src.models.portfolio import (
    Holding,
    Portfolio,
    PortfolioAllocation,
    PortfolioCreate,
    PortfolioValuation,
)
from src.services.portfolio_service import PortfolioService


router = APIRouter(prefix="/portfolio", tags=["Portfolio"])


_service = PortfolioService()


def get_portfolio_service() -> PortfolioService:
    return _service


@router.post("", response_model=Portfolio)
def create_portfolio(
    payload: PortfolioCreate,
    service: PortfolioService = Depends(get_portfolio_service),
):
    return service.create_portfolio(
        name=payload.name,
        base_currency=payload.base_currency,
    )


@router.get("/{portfolio_id}", response_model=Portfolio)
def get_portfolio(
    portfolio_id: str,
    service: PortfolioService = Depends(get_portfolio_service),
):
    portfolio = service.get_portfolio(portfolio_id)

    if portfolio is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return portfolio


@router.post(
    "/{portfolio_id}/holdings",
    response_model=Portfolio,
)
def add_holding(
    portfolio_id: str,
    holding: Holding,
    service: PortfolioService = Depends(get_portfolio_service),
):
    portfolio = service.add_holding(
        portfolio_id=portfolio_id,
        holding=holding,
    )

    if portfolio is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return portfolio


@router.get(
    "/{portfolio_id}/allocation",
    response_model=PortfolioAllocation,
)
def get_allocation(
    portfolio_id: str,
    service: PortfolioService = Depends(get_portfolio_service),
):
    allocation = service.get_allocation(portfolio_id)

    if allocation is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return allocation


@router.get(
    "/{portfolio_id}/allocation/live",
    response_model=PortfolioAllocation,
)
def get_live_allocation(
    portfolio_id: str,
    service: PortfolioService = Depends(get_portfolio_service),
):
    allocation = service.get_live_allocation(portfolio_id)

    if allocation is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return allocation



@router.get(
    "/{portfolio_id}/valuation",
    response_model=PortfolioValuation,
)
def get_valuation(
    portfolio_id: str,
    service: PortfolioService = Depends(get_portfolio_service),
):
    valuation = service.get_valuation(portfolio_id)

    if valuation is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return valuation
