from sqlalchemy import Column, Integer, Float

from sensors.core.database import *


class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True)
    lat = Column(Float)
    lon = Column(Float)
