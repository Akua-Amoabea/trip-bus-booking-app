from app.config.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
import uuid


class Location(Base):
    __tablename__ = "locations"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name=Column(String, nullable=False, unique=True)
    