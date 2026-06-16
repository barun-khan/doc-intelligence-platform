from fastapi import FastAPI
from backend.utils.config import config

# Validate configuration on startup
# config.validate()

# Create FastAPI app
app = FastAPI(
    title="Document Intelligence Platform",
    description="Enterprise RAG-based document intelligence system",
    version="0.1.0"
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": "Document Intelligence Platform",
        "version": "0.1.0"
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Document Intelligence Platform",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)