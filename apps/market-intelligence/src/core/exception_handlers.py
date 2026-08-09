import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions.provider import ProviderError

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers.
    """

    @app.exception_handler(ProviderError)
    async def provider_error_handler(
        request: Request,
        exc: ProviderError,
    ):
        logger.error(
            "Provider request failed",
            extra={
                "path": request.url.path,
                "error": str(exc),
            },
        )

        return JSONResponse(
            status_code=503,
            content={
                "status": "error",
                "code": "PROVIDER_ERROR",
                "message": str(exc),
            },
        )