"""Service layer for VM operations."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from ..models import VMCreate, VM
from ..database import VM as VMModel

class VMService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_vm(self, vm_in: VMCreate) -> VM:
        # Insert into DB
        stmt = insert(VMModel).values(
            name=vm_in.name,
            cpu=vm_in.cpu,
            memory_gb=vm_in.memory_gb,
            storage_gb=vm_in.storage_gb,
            host_id=vm_in.host_id,
            status="running"
        ).returning(VMModel)
        result = await self.db.execute(stmt)
        await self.db.commit()
        vm_row = result.fetchone()
        return VM.from_orm(vm_row)

    async def list_vms(self) -> list[VM]:
        stmt = select(VMModel)
        result = await self.db.execute(stmt)
        rows = result.scalars().all()
        return [VM.from_orm(row) for row in rows]
