import uuid
from app.config.database import Base
from sqlalchemy import Column,  ForeignKey, Integer, Float
from sqlalchemy.dialects.postgresql import UUID


class Luggage(Base):
    __tablename__ = "luggages"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_uuid=Column(UUID(as_uuid=True), ForeignKey("bookings.uuid"), nullable=False)
    number_of_luggages=Column(Integer, nullable=False)
    weight_of_luggages=Column(Float, nullable=False)
    price = Column(Float,nullable=False)
