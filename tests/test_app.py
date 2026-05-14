from src.app import Handler


def test_handler_class_exists() -> None:
    # Smoke: the class symbol exists and inherits from BaseHTTPRequestHandler.
    from http.server import BaseHTTPRequestHandler

    assert issubclass(Handler, BaseHTTPRequestHandler)
