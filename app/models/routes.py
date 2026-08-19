from datetime import datetime, timezone
import uuid

from app.config.database import Base
from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean, Date, Time, Float
from sqlalchemy.dialects.postgresql import UUID


class Route(Base):
    __tablename__ = "routes"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    leaving_time=Column(Time, nullable=False)
    destination_time = Column(Time, nullable=False)
    created_time = Column(DateTime(timezone=True),nullable=False,default=lambda: datetime.now(timezone.utc))
    location_uuid = Column(UUID(as_uuid=True),ForeignKey("locations.uuid"),nullable=False)
    destination_uuid = Column(
        UUID(as_uuid=True),ForeignKey("locations.uuid"),nullable=False
    )
    price = Column(Float, nullable=False)    
    leaving_date = Column(Date, nullable=False) 
    bus_uuid = Column(UUID(as_uuid=True), ForeignKey("buses.uuid"), nullable=False)
    
    