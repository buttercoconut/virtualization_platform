# main.py
from fastapi import FastAPI
from .database import init_db
from .routers import vm_router

app = FastAPI(title="Virtualization Platform API", version="0.1.0")

app.include_router(vm_router.router)

@app.on_event("startup")
async def startup_event():
    await init_db()

# Optional: health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
