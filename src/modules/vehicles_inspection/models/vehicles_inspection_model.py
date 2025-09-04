import uuid
from enum import Enum
from sqlalchemy import Column, Boolean, String, DateTime, ForeignKey, Enum as SqlEnum, UUID
from sqlalchemy.sql import func

from src.database.connection import Base

class Shift(str, Enum):
    MORNING = "MORNING"
    EVENING = "EVENING"

class InspectionStatus(str, Enum):
    OK = "OK"
    MINOR_ISSUE = "MINOR_ISSUE"
    MAJOR_ISSUE = "MAJOR_ISSUE"

class VehicleInspection(Base):
    __tablename__ = "vehicle_inspections"
    __table_args__ = {"schema": "natudrive"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    driver_id = Column(UUID(as_uuid=True), ForeignKey("natudrive.drivers.id"), nullable=False)
    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("natudrive.vehicles.id"), nullable=False)
    inspection_date = Column(DateTime, default=func.now(), nullable=False)
    shift = Column(SqlEnum(Shift), nullable=False)
    notes = Column(String)
    status = Column(SqlEnum(InspectionStatus), default=InspectionStatus.OK)