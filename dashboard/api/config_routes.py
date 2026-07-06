from fastapi import APIRouter
from core.config.config_service import ConfigService

router = APIRouter()

service = ConfigService()


@router.get("/config")
def get_config():

    return service.get_config()


@router.post("/config/update")
def update_config(key: str, value: str):

    service.update_config(key, value)

    return {"status": "updated", "key": key}


@router.get("/config/validate")
def validate():

    return service.validate()