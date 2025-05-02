# app/main.py

import time
from fastapi import (
    FastAPI,
    Request
)
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.utils.logger import logger
from app.api.v1.outfit import router as outfit_router

# Create the FastAPI application
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    print("Starting up the application...")
    try:
        yield
    finally:
        print("Shutting down the application...")

app = FastAPI(
    title=settings.APP_NAME,
    description="An API",
    version="1.0.0",
    debug=settings.DEBUG,  # Enable debug mode if in development
    lifespan=lifespan,
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(outfit_router)



# Middleware to log route endpoints
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    endpoint = request.url.path
    method = request.method
    client_ip = request.client.host

    logger.info(f"Request: {method} {endpoint} from {client_ip}")
    
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.info(f"Response: {method} {endpoint} returned {response.status_code} in  {process_time:.2f} seconds")
    return response



# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": f"{settings.APP_NAME} is running"}
