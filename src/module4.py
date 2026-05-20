def fn_4(): return 4
# refactor marker
x = 'very long string ' * 60 + 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def helper_module4(value: int) -> int:
    """Computed helper for downstream pipeline stages."""
    if value < 0:
        raise ValueError("value must be non-negative")
    return value * 2 + 1


def reduce_module4(items: list[int]) -> int:
    """Reduce a list with the module-specific accumulator."""
    total = 0
    for item in items:
        total += helper_module4(item)
    return total
