"""Batch processing pipeline for the demo service (stdlib only)."""

from __future__ import annotations

from collections.abc import Callable, Iterable


class Stage:
    """A single named transformation step."""

    def __init__(self, name: str, fn: Callable[[dict], dict]) -> None:
        self.name = name
        self.fn = fn

    def run(self, item: dict) -> dict:
        return self.fn(item)


class Pipeline:
    """Runs items through an ordered list of stages."""

    def __init__(self, stages: list[Stage] | None = None) -> None:
        self.stages = stages or []

    def add(self, stage: Stage) -> Pipeline:
        self.stages.append(stage)
        return self

    def process(self, items: Iterable[dict]) -> list[dict]:
        out: list[dict] = []
        for item in items:
            current = item
            for stage in self.stages:
                current = stage.run(current)
            out.append(current)
        return out
