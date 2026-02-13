from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from src.router.item_router import router as item_router
from src.core.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Item Management API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(item_router)

@app.get("/")
async def root():
    return RedirectResponse(url="/scalar")

@app.get("/scalar", include_in_schema=False)
async def scalar_api_reference():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title + " - Scalar",
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "SQLite"}