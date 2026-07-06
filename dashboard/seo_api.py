from fastapi import APIRouter

router = APIRouter()


@router.get("/seo/report")
def report():

    return {"status": "seo module active"}