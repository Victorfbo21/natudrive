
from sqlalchemy import Column, UUID, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from src.database.connection import Base


class Driver(Base):
    __tablename__ = "drivers"
    __table_args__ = {"schema": "natudrive"}

    id = Column(UUID(as_uuid=True), ForeignKey("natudrive.users.id"), primary_key=True)
    driver_license = Column(String, nullable=False)
    license_category = Column(String)  # A, B, C, D, E
    license_expiration = Column(DateTime, nullable=False)
    emergency_contact = Column(String)
    updated_at = Column(DateTime)
    updated_by = Column(UUID, ForeignKey('natudrive.users.id'))

    user = relationship("Users", back_populates="driver_profile")
