from datetime import datetime, timezone
import uuid

from app.config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Seats(Base):
    __tablename__ = "seats"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seat_number=Column(String, nullable=False)
    is_available=Column(Boolean,nullable=False)
    route_uuid=Column(UUID(as_uuid=True), ForeignKey=("routes.uuid"), nullable=False)
    bus_uuid=Column(UUID(as_uuid=True), ForeignKey=("buses.uuid"), nullable=False)