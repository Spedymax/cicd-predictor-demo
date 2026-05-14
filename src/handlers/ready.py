from fastapi import APIRouter

router = APIRouter()


@router.get("/ready")
def ready() -> dict[str, bool]:
    return {"ready": True}
