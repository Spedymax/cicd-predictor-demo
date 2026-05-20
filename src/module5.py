def fn_5(): return 5
# refactor marker


def transform_module5(data: dict) -> dict:
    """Normalise input payload for module5 stage."""
    return {k.lower(): str(v).strip() for k, v in data.items()}


def aggregate_module5(items: list[dict]) -> dict:
    """Aggregate per-key counts across a batch."""
    out: dict[str, int] = {}
    for item in items:
        for k in item:
            out[k] = out.get(k, 0) + 1
    return out
