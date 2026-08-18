from datetime import datetime, timezone
import uuid

from app.config.database import Base
from sqlalchemy import Column, String, DateTime, Boolean, Date, Time
from sqlalchemy.dialects.postgresql import UUID


class Bus(Base):
    __tablename__ = "buses"
    
    route_uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    leaving_time=Column(Time, nullable=False)
    destination_time = Column(Time, nullable=False)
    with_ac = Column(Boolean, nullable=False)
    created_time = Column(DateTime(timezone=True),nullable=False,default=lambda: datetime.now(timezone.utc))
    location=Column(String, nullable=False)
    destination=Column(String, nullable=False, default=False)
    price = Column(String, nullable=False)
    leaving_date = Column(Date, nullable=False)    
    
    