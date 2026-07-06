from fastapi import APIRouter

router = APIRouter()


@router.get("/evaluation")
def evaluation():

    return {"status": "evaluation module active"}