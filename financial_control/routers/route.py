from fastapi import APIRouter

api = APIRouter(prefix='/api')
web = APIRouter(prefix='')

@web.get('/')
def hello_world():
    return {"ping": "pong"}

@api.get('/')
def hello_world():
    return {"app_name": "Financial Control"}