def fn_1(): return 1
# trivial inline comment


def helper_module1(value: int) -> int:
    """Computed helper for downstream pipeline stages."""
    if value < 0:
        raise ValueError("value must be non-negative")
    return value * 2 + 1


def reduce_module1(items: list[int]) -> int:
    """Reduce a list with the module-specific accumulator."""
    total = 0
    for item in items:
        total += helper_module1(item)
    return total

# helper utilities for demo-warn branch
