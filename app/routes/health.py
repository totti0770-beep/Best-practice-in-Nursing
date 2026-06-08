from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/", summary="API root")
def root() -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Best Nursing Practice AI backend is running",
    }


@router.get("/health", summary="Service health")
def health() -> dict[str, str]:
    return {"status": "healthy"}
