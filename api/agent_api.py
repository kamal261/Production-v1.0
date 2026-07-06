from fastapi import APIRouter

from agent.agent import SEOAgent

router = APIRouter()


agent = SEOAgent()


@router.get("/audit")
def audit(url: str):

    return agent.audit(url)