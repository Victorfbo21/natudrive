import uuid
from enum import Enum
from sqlalchemy import  Column, UUID, String, Integer, DateTime, Boolean, Enum as SqlEnum
from src.database.connection import Base

class FuelType(str, Enum):
    GASOLINE = "GASOLINE"
    DIESEL = "DIESEL"
    ETHANOL = "ETHANOL"
    ELECTRIC = "ELECTRIC"
    HYBRID = "HYBRID"

class VehicleType(str, Enum):
    CAR = "CAR"
    TRUCK = "TRUCK"

class VehicleStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    IN_USE = "IN_USE"
    MAINTENANCE = "MAINTENANCE"
    INACTIVE = "INACTIVE"


class Vehicle(Base):
    __tablename__ = "vehicles"
    __table_args__ = {"schema": "natudrive"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plate = Column(String, unique=True, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    vehicle_type = Column(SqlEnum(VehicleType), nullable=False)
    fuel_type = Column(SqlEnum(FuelType), nullable=False)
    odometer = Column(Integer, default=0)
    status = Column(SqlEnum(VehicleStatus), default=VehicleStatus.AVAILABLE)
    is_active = Column(Boolean, default=True)

    license_expiration = Column(DateTime)
    inspection_expiration = Column(DateTime, nullable=True)
    insurance_expiration = Column(DateTime, nullable=True)