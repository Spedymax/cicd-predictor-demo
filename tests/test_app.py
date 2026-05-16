"""Smoke + import-coverage tests for the demo service."""

import importlib

import pytest

from src.app import Handler

MODULE_NAMES = [f"src.module{i}" for i in range(1, 13)]


def test_handler_class_exists() -> None:
    from http.server import BaseHTTPRequestHandler

    assert issubclass(Handler, BaseHTTPRequestHandler)


def test_handler_has_do_get() -> None:
    assert callable(getattr(Handler, "do_GET", None))


@pytest.mark.parametrize("name", MODULE_NAMES)
def test_module_imports_cleanly(name: str) -> None:
    importlib.import_module(name)


def test_all_module_names_distinct() -> None:
    assert len(set(MODULE_NAMES)) == len(MODULE_NAMES)
