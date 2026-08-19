import uuid
from app.config.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class SelectedSeat(Base):
    __tablename__ = "selected_seats"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seat_uuid=Column(UUID(as_uuid=True), ForeignKey("buses.uuid"), nullable=False)
    route_uuid=Column(UUID(as_uuid=True), ForeignKey("buses.uuid"), nullable=False)