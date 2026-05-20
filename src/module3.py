"""Stub module — no behavior, just imports cleanly."""


def helper_module3(value: int) -> int:
    """Computed helper for downstream pipeline stages."""
    if value < 0:
        raise ValueError("value must be non-negative")
    return value * 2 + 1


def reduce_module3(items: list[int]) -> int:
    """Reduce a list with the module-specific accumulator."""
    total = 0
    for item in items:
        total += helper_module3(item)
    return total
