"""Lightweight in-memory request metrics for the demo service."""

from __future__ import annotations

import time
from collections import defaultdict


class MetricsRegistry:
    """Counter/timer registry with no external dependencies."""

    def __init__(self) -> None:
        self._counters: dict[str, int] = defaultdict(int)
        self._timers: dict[str, float] = defaultdict(float)

    def incr(self, name: str, value: int = 1) -> None:
        self._counters[name] += value

    def observe(self, name: str, seconds: float) -> None:
        self._timers[name] += seconds

    def snapshot(self) -> dict[str, float]:
        merged: dict[str, float] = {}
        merged.update({f"count.{key}": val for key, val in self._counters.items()})
        merged.update({f"time.{key}": round(val, 4) for key, val in self._timers.items()})
        return merged


def measure(registry: MetricsRegistry, name: str):
    """Record wall-clock time of the wrapped function into the registry."""

    def wrap(fn):
        def inner(*args, **kwargs):
            start = time.perf_counter()
            try:
                return fn(*args, **kwargs)
            finally:
                registry.observe(name, time.perf_counter() - start)

        return inner

    return wrap
