from fastapi import APIRouter

router = APIRouter()


@router.post("/run")
def run():

    return {"status": "autopilot queued"}