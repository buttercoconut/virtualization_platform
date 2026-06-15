from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import VMCreateRequest, VMResponse
from .services.vm_service import create_vm

router = APIRouter()

@router.post("/", response_model=VMResponse)
async def create_vm_endpoint(vm_req: VMCreateRequest, db: Session = Depends(SessionLocal)):
    vm = create_vm(db, vm_req)
    return vm
