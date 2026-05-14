import logging

import structlog
from fastapi import FastAPI


def attach(app: FastAPI) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    structlog.configure(
        processors=[structlog.processors.JSONRenderer()],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    )
    app.state.log = structlog.get_logger("app")
