import uvicorn
from fastapi import FastAPI

from financial_control.routers import route

app = FastAPI()

app.include_router(route.api)
app.include_router(route.web)

if __name__ == '__main__':
    uvicorn.run(app)