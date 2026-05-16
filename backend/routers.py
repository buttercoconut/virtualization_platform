"""Router for VM endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from ..services.vm_service import VMService
from ..models import VMCreate, VM

vm_router = APIRouter()

@vm_router.post("/", response_model=VM, status_code=status.HTTP_201_CREATED)
async def create_vm(vm_in: VMCreate, db: AsyncSession = Depends(get_db)):
    service = VMService(db)
    try:
        vm = await service.create_vm(vm_in)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return vm

@vm_router.get("/", response_model=list[VM])
async def list_vms(db: AsyncSession = Depends(get_db)):
    service = VMService(db)
    return await service.list_vms()
