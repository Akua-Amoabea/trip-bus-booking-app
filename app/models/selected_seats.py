import uuid
from app.config.database import Base
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID


class SelectedSeat(Base):
    __tablename__ = "selected_seats"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seat_uuid=Column(UUID(as_uuid=True), ForeignKey("seats.uuid"), nullable=False)
    route_uuid=Column(UUID(as_uuid=True), ForeignKey("routes.uuid"), nullable=False)
    booking_uuid=Column(UUID(as_uuid=True), ForeignKey("bookings.uuid"), nullable=False)
    
    
    __table_args__ = (
        UniqueConstraint(
            "route_uuid",
            "seat_uuid",
            name="uq_selected_seat_route"
        ),
    )