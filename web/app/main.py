from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

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
