# services/vm_service.py
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..database import Base, engine
from ..api.models import VMCreate, VM
from sqlalchemy import Column, Integer, String, ForeignKey

# Simple ORM model for demonstration
class VMModel(Base):
    __tablename__ = "vms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    cpu = Column(Integer)
    memory_gb = Column(Integer)
    storage_gb = Column(Integer)
    host_id = Column(Integer, ForeignKey("hosts.id"))
    status = Column(String, default="stopped")

async def create_vm(db: AsyncSession, vm_in: VMCreate) -> VMModel:
    vm = VMModel(**vm_in.dict())
    db.add(vm)
    await db.commit()
    await db.refresh(vm)
    return vm

async def list_vms(db: AsyncSession) -> List[VMModel]:
    result = await db.execute(select(VMModel))
    return result.scalars().all()
