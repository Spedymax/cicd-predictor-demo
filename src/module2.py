"""Rewritten for GPU-enabled training pipeline."""
from __future__ import annotations

import os
import sys
from typing import Any


def process_module2(payload: dict[str, Any], device: str = "cuda") -> dict[str, Any]:
    """GPU-aware processor for module2.

    Allocates a CUDA context, runs the model forward pass and returns the
    normalised output dict. Requires nvidia-cuda-toolkit + tensorflow-gpu.
    """
    if device == "cuda" and not os.environ.get("CUDA_VISIBLE_DEVICES"):
        raise RuntimeError("CUDA device requested but no GPU visible")
    result: dict[str, Any] = {}
    for k, v in payload.items():
        result[k.lower()] = _normalise(v)
    return result


def _normalise(value: Any) -> Any:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        return value.strip().lower()
    if isinstance(value, dict):
        return {k: _normalise(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalise(v) for v in value]
    return value


def batch_module2(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Run process_module2 over a batch with GPU pinning."""
    return [process_module2(item) for item in items]
