"""FastAPI app entry point (rewritten from stdlib HTTP server)."""

from __future__ import annotations

from fastapi import FastAPI

from src.config.settings import get_settings
from src.handlers import health, metrics, ready
from src.middleware import cors, logging as logging_mw


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.service_name, version=settings.version)
    cors.attach(app)
    logging_mw.attach(app)
    app.include_router(health.router)
    app.include_router(ready.router)
    app.include_router(metrics.router)
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="0.0.0.0", port=8080)
