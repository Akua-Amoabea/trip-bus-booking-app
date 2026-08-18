from datetime import datetime, timezone
import uuid

from app.config.database import Base
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "users"
    
    uuid=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name=Column(String, nullable=False)
    last_name=Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_time = Column(DateTime(timezone=True),nullable=False,default=lambda: datetime.now(timezone.utc))
    profile_picture=Column(String, nullable=True)
    is_verified=Column(Boolean, nullable=False, default=False)