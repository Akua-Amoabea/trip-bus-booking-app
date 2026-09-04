import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base
from sqlalchemy import Column, ForeignKey, String


class Booking(Base):
    __tablename__ = 'bookings'
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    route_uuid= Column(UUID(as_uuid=True), ForeignKey("routes.uuid"), nullable=False)
    user_uuid= Column(UUID(as_uuid=True), ForeignKey("users.uuid"), nullable=False)
    status = Column(String,nullable=False)
    
    
    
    
 