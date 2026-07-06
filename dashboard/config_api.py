from fastapi import APIRouter
from core.config.config_service import ConfigService

router = APIRouter()

service = ConfigService()


@router.get("/config")
def get_config():

    return service.all()


@router.post("/config/set")
def set_config(key: str, value: str):

    service.set(key, value)

    return {"status": "updated"}