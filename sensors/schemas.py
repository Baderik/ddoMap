from pydantic import BaseModel

__all__ = ["Sensor", "SensorCreate"]


class SensorBase(BaseModel):
    lat: float
    lon: float


class Sensor(SensorBase):
    id: int

    class Config:
        orm_mode = True


class SensorCreate(SensorBase):
    pass
