from fastapi import FastAPI
from routes.routes import router

app = FastAPI(
    title="Market Trade Opportunity Analyzer",
    description="AI-powered market analysis for Indian sectors",
    version="1.0.0"
)
#
app.include_router(router)