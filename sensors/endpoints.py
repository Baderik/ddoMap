from fastapi import APIRouter, Depends, HTTPException

from sensors import schemas, crud
from sensors.core import database

database.create_tables()  # TODO: Move this to main mange file

router = APIRouter()


@router.post("/", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorCreate, db: database.Session = Depends(database.get_db)):
    return crud.create_sensor(db, sensor)


@router.get("/{sid:int}/", response_model=schemas.Sensor)
def read_sensor(sid: int, db: database.Session = Depends(database.get_db)):
    sensor_model = crud.get_sensor(db, sid=sid)
    if sensor_model is None:
        raise HTTPException(status_code=404, detail="This is not the sensor you are looking for.")
    return sensor_model


@router.get("/", response_model=list[schemas.Sensor])
def read_sensors(skip: int = 0, limit: int = 100, db: database.Session = Depends(database.get_db)):
    return crud.get_sensors(db, skip=skip, limit=limit)
