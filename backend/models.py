# models.py
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .database import Base

class VMStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"

class VM(Base):
    __tablename__ = "vms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    cpu = Column(Integer, nullable=False)
    memory = Column(Integer, nullable=False)  # in MB
    status = Column(Enum(VMStatus), default=VMStatus.PENDING, nullable=False)

    snapshots = relationship("Snapshot", back_populates="vm")

class Snapshot(Base):
    __tablename__ = "snapshots"

    id = Column(Integer, primary_key=True, index=True)
    vm_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    vm = relationship("VM", back_populates="snapshots")
