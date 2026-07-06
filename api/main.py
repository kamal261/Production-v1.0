from fastapi import FastAPI

from dashboard.seo_api import router as seo_router
from dashboard.keyword_api import router as keyword_router
from dashboard.competitor_api import router as competitor_router
from dashboard.ranking_api import router as ranking_router

app = FastAPI(title="SEO AI Platform")

app.include_router(seo_router)
app.include_router(keyword_router)
app.include_router(competitor_router)
app.include_router(ranking_router)