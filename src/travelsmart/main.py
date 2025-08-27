import uvicorn
from fastapi import FastAPI
from travelsmart.config import settings
from travelsmart.logging_config import configure_logging
from travelsmart.api.routes import router as api_router

configure_logging()
app = FastAPI(title="travelsmart-ai-service", version="1.0")

app.include_router(api_router, prefix="/api/v1")

@app.get("/healthz")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("travelsmart.main:app", host=settings.HOST, port=settings.PORT, reload=False)
