def fn_7(): return 7
# refactor marker


def transform_module7(data: dict) -> dict:
    """Normalise input payload for module7 stage."""
    return {k.lower(): str(v).strip() for k, v in data.items()}


def aggregate_module7(items: list[dict]) -> dict:
    """Aggregate per-key counts across a batch."""
    out: dict[str, int] = {}
    for item in items:
        for k in item:
            out[k] = out.get(k, 0) + 1
    return out
