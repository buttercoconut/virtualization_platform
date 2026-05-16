"""FastAPI application entry point for the virtualization platform backend."""

from fastapi import FastAPI
from .routers import vm_router

app = FastAPI(title="Virtualization Platform API")

# Include routers
app.include_router(vm_router, prefix="/v1/vms", tags=["VMs"])

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Virtualization Platform API"}
