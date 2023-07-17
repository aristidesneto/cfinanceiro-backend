import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from financial_control.core.config import settings
from financial_control.apis.base import router

app = FastAPI(title=settings.APP_NAME)

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app)