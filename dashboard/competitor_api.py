from fastapi import APIRouter

router = APIRouter()


@router.get("/competitors")
def competitors():

    return {"competitors": []}