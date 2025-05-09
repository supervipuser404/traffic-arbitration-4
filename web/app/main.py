from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

from web.app.services.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(
    title="News Showcase Web",
    description="Dynamic news feed with native ads",
    version="0.1.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="web/app/static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="web/app/templates")


@app.get("/")
async def root():
    return {"message": "Welcome to News Showcase Web"}


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"}, status_code=200)


@app.get("/db-test")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        # Простой запрос для проверки подключения
        await db.execute("SELECT 1")
        return {"message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
