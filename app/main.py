from fastapi import FastAPI

app = FastAPI(title="Best Nursing Practice AI API")


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "message": "Best Nursing Practice AI backend is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}
