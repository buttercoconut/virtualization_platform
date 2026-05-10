# api/routers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from ..services.vm_service import create_vm, list_vms
from .models import VMCreate, VM

router = APIRouter(prefix="/vms", tags=["VMs"])

@router.post("/", response_model=VM)
async def create_vm_endpoint(vm_in: VMCreate, db: AsyncSession = Depends(get_session)):
    try:
        vm = await create_vm(db, vm_in)
        return vm
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[VM])
async def list_vms_endpoint(db: AsyncSession = Depends(get_session)):
    vms = await list_vms(db)
    return vms
