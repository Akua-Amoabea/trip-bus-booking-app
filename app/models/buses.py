import uuid

from app.config.database import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID


class Bus(Base):
    __tablename__ = "buses"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bus_number=Column(String, nullable=False, unique=True)
    with_ac = Column(Boolean, nullable=False)
    capacity=Column(Integer, nullable=False)
    