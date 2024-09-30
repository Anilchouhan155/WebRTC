# app/main.py

from fastapi import FastAPI
from app.routers import calls

app = FastAPI(
    title="WebRTC Signaling Server",
    description="Backend API for WebRTC Signaling",
    version="1.0.0",
)

# Include the calls router
app.include_router(calls.router, tags=["Calls"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "WebRTC Signaling Server is running"}
