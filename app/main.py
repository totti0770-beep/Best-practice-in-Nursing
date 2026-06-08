from fastapi import APIRouter, FastAPI

from app.routes.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Best Nursing Practice AI API",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    api_v1 = APIRouter(prefix="/api/v1")
    api_v1.include_router(health_router)
    app.include_router(api_v1)
    return app


app = create_app()
