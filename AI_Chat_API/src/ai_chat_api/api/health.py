
from ai_chat_api.config import settings

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "Status":"Healthy",
        "App_name":settings.app_name,
        "version": settings.app_version
    }