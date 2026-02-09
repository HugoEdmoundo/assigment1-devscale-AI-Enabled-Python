from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from src.router.item_router import router as item_router
from src.core.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables
    create_db_and_tables()
    yield
    # Shutdown: nothing to do

# Create FastAPI app
app = FastAPI(
    title="Item Management API",
    description="API for managing items with SQLModel and SQLite",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(item_router)

@app.get("/")
async def root():
    """Redirect to Scalar API documentation"""
    return RedirectResponse(url="/scalar")

@app.get("/scalar", include_in_schema=False)
async def scalar_api_reference():
    """Scalar API Documentation"""
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title + " - Scalar",
    )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "database": "SQLite"}