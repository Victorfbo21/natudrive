from src.database.connection import Base
from sqlalchemy import Column, String, DateTime, Boolean, Enum as SqlEnum, ForeignKey, UUID
import uuid
from enum import Enum
from sqlalchemy.sql import func

class UserType(str, Enum):
    USER= 'USER'
    ADMIN = 'ADMIN'

class Users(Base):

    __tablename__ = "users"
    __table_args__ = {"schema" : "natudrive"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    user_type = Column(SqlEnum(UserType))
    updated_at = Column(DateTime, onupdate=func.now())
    updated_by = Column(UUID, ForeignKey("natudrive.users.id"), nullable=True)
    created_at = Column(DateTime, default=func.now())
    created_by = Column(UUID, ForeignKey("natudrive.users.id"), nullable=False)
