def fn_8(): return 8
# refactor marker


def transform_module8(data: dict) -> dict:
    """Normalise input payload for module8 stage."""
    return {k.lower(): str(v).strip() for k, v in data.items()}


def aggregate_module8(items: list[dict]) -> dict:
    """Aggregate per-key counts across a batch."""
    out: dict[str, int] = {}
    for item in items:
        for k in item:
            out[k] = out.get(k, 0) + 1
    return out
