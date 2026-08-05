from ai_chat_api.config import settings
from ai_chat_api.core.logging import logger
from ai_chat_api.api.health import router
from fastapi import FastAPI

logger.info("Application is started......")

app=FastAPI()
app.include_router(router)

print("hello from main")
print(settings.app_name)
print(settings.port)


