from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI application instance
app = FastAPI(title="Boston Startup Tracker API", openapi_url=f"{settings.API_PREFIX}/openapi.json")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_PREFIX)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Boston Startup Tracker API"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)