from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

# Import routers
from api.crm_api import router as crm_router
from api.engagement_api import router as engagement_router
from api.market_api import router as market_router
from api.kb_api import router as kb_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Customer Data Mock APIs",
    description="Mock APIs for customer analysis platform demonstration",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(crm_router, prefix="/crm", tags=["CRM"])
app.include_router(engagement_router, prefix="/engagement", tags=["Engagement"])
app.include_router(market_router, prefix="/market", tags=["Market Intelligence"])
app.include_router(kb_router, prefix="/kb", tags=["Knowledge Base"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Customer Analysis Platform Mock APIs",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run the Customer 360 Data APIs server")
    parser.add_argument("--port", type=int, default=8000, help="Port number for the server (default: 8000)")
    args = parser.parse_args()
    
    print(f"Starting HTTP server on http://localhost:{args.port}...")
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=args.port,
        reload=True  # Enable auto-reload during development
    )