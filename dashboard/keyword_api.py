from fastapi import APIRouter

router = APIRouter()


@router.get("/keywords")
def keywords():

    return {"keywords": []}