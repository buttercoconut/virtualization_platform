from fastapi import FastAPI, APIRouter, Depends
from .database import SessionLocal
from .models import VMCreateRequest
from .services import vm_service

app = FastAPI()

# Dependency for DB session
@app.on_event("startup")
async def startup():
    # Initialize DB connection if needed
    pass

# Include router
app.include_router(vm_router, prefix="/vms")
