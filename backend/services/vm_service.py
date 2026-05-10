# services/vm_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import VM, VMStatus
from ..schemas import VMCreate

class VMService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_vm(self, vm_in: VMCreate) -> VM:
        vm = VM(**vm_in.dict(), status=VMStatus.PENDING)
        self.db.add(vm)
        await self.db.commit()
        await self.db.refresh(vm)
        return vm

    async def get_vm(self, vm_id: int) -> VM | None:
        result = await self.db.execute(select(VM).where(VM.id == vm_id))
        return result.scalar_one_or_none()

    async def list_vms(self):
        result = await self.db.execute(select(VM))
        return result.scalars().all()
