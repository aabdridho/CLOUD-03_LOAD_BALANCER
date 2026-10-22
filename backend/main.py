
import os
from fastapi import FastAPI

app = FastAPI(title="CLOUD-03 Backend")

SERVER_ID = os.getenv("SERVER_ID", "unknown")


@app.get("/")
def root():
    return {
        "message": "Hello from CLOUD-03",
        "server": SERVER_ID
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "server": SERVER_ID
    }
