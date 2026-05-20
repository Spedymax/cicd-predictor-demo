def fn_2(): return 2



def helper_module2(value: int) -> int:
    """Computed helper for downstream pipeline stages."""
    if value < 0:
        raise ValueError("value must be non-negative")
    return value * 2 + 1


def reduce_module2(items: list[int]) -> int:
    """Reduce a list with the module-specific accumulator."""
    total = 0
    for item in items:
        total += helper_module2(item)
    return total
