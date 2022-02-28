from fastapi import APIRouter

from app.api.endpoints import initial

# Routes for our app
api_router = APIRouter()
api_router.include_router(initial.router)
