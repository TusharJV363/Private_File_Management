from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.models import user
from app.api.routes.health import router as health_router

Base.metadata.create_all(bind=engine)

app=FastAPI(title=settings.APP_NAME)

app.include_router(health_router)

@app.get("/")
def root():
    return {"status" : "Backend is running ... "}