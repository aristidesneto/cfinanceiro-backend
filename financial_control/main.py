import uvicorn

from fastapi import FastAPI

from financial_control.core.config import settings
from financial_control.apis.base import router

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app)