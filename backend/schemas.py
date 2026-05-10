# schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class VMStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"

class VMBase(BaseModel):
    name: str = Field(..., example="web-server-01")
    cpu: int = Field(..., example=4)
    memory: int = Field(..., example=8192)  # MB

class VMCreate(VMBase):
    pass

class VMRead(VMBase):
    id: int
    status: VMStatus

    class Config:
        orm_mode = True
