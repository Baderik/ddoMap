from fastapi import APIRouter

from sensors.endpoints import router as sensors

router = APIRouter()
router.include_router(sensors, prefix="/sensors", tags=["Sensors"])
