from sqlalchemy.orm import Session
from .models import VMCreateRequest, VMResponse

# Dummy implementation

def create_vm(db: Session, vm_req: VMCreateRequest) -> VMResponse:
    # In real code, insert into DB and return created VM
    return VMResponse(
        id=1,
        name=vm_req.name,
        cpu=vm_req.cpu,
        memory_gb=vm_req.memory_gb,
        storage_gb=vm_req.storage_gb,
        status="running",
        host_id=vm_req.host_id,
    )
