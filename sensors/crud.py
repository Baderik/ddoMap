from sqlalchemy.orm import Session

from sensors import models, schemas


def get_sensor(db: Session, sid: int) -> models.Sensor:
    return db.query(models.Sensor).filter(models.Sensor.id == sid).first()


def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sensor).offset(skip).limit(limit).all()


def create_sensor(db: Session, sensor: schemas.SensorCreate) -> models.Sensor:
    sensor_model = models.Sensor(lat=sensor.lat, lon=sensor.lon)
    db.add(sensor_model)
    db.commit()
    db.refresh(sensor_model)
    return sensor_model
