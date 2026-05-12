from fastapi import APIRouter, FastAPI

app = FastAPI(title="Best Nursing Practice AI API")
api_router = APIRouter(prefix="/api/v1")


@api_router.get("/")
def root() -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Best Nursing Practice AI backend is running",
    }


@api_router.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


app.include_router(api_router)
