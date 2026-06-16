"""Minimal cooperative task scheduler (stdlib only)."""

from __future__ import annotations

import heapq
from collections.abc import Callable


class Scheduler:
    """Priority queue of due tasks keyed by a numeric timestamp."""

    def __init__(self) -> None:
        self._queue: list[tuple[float, int, Callable[[], None]]] = []
        self._seq = 0

    def schedule(self, at: float, task: Callable[[], None]) -> None:
        heapq.heappush(self._queue, (at, self._seq, task))
        self._seq += 1

    def run_due(self, now: float) -> int:
        ran = 0
        while self._queue and self._queue[0][0] <= now:
            _, _, task = heapq.heappop(self._queue)
            task()
            ran += 1
        return ran

    def pending(self) -> int:
        return len(self._queue)
