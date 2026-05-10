# routers/vm_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import async_session
from ..schemas import VMCreate, VMRead
from ..services.vm_service import VMService

router = APIRouter(prefix="/vms", tags=["Virtual Machines"])

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

@router.post("/", response_model=VMRead, status_code=status.HTTP_201_CREATED)
async def create_vm(vm_in: VMCreate, db: AsyncSession = Depends(get_db)):
    service = VMService(db)
    vm = await service.create_vm(vm_in)
    return vm

@router.get("/", response_model=list[VMRead])
async def list_vms(db: AsyncSession = Depends(get_db)):
    service = VMService(db)
    return await service.list_vms()

@router.get("/{vm_id}", response_model=VMRead)
async def get_vm(vm_id: int, db: AsyncSession = Depends(get_db)):
    service = VMService(db)
    vm = await service.get_vm(vm_id)
    if not vm:
        raise HTTPException(status_code=404, detail="VM not found")
    return vm
