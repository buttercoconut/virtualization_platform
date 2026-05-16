"""Pydantic models for VM and related entities."""

from pydantic import BaseModel, Field
from typing import Optional

class VMBase(BaseModel):
    name: str = Field(..., example="web-server-01")
    cpu: int = Field(..., ge=1, example=2)
    memory_gb: int = Field(..., ge=1, example=4)
    storage_gb: int = Field(..., ge=1, example=50)
    host_id: Optional[int] = Field(None, example=1)

class VMCreate(VMBase):
    pass

class VM(VMBase):
    id: int
    status: str = Field(..., example="running")

    class Config:
        orm_mode = True
