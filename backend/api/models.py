from pydantic import BaseModel, Field
from typing import Optional

class VMCreateRequest(BaseModel):
    name: str = Field(..., example="web-server-01")
    cpu: int = Field(..., ge=1, example=2)
    memory_gb: int = Field(..., ge=1, example=4)
    storage_gb: int = Field(..., ge=10, example=50)
    host_id: Optional[int] = Field(None, example=1)

class VMResponse(BaseModel):
    id: int
    name: str
    cpu: int
    memory_gb: int
    storage_gb: int
    status: str
    host_id: Optional[int]

# In a real implementation, these would be ORM models
