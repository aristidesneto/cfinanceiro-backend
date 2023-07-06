from fastapi import APIRouter, HTTPException

from financial_control.schemas.user import UserCreateSchema
from financial_control.services.user import UserService

from financial_control.schemas.income import IncomeCreateSchema
from financial_control.services.income import IncomeService

api = APIRouter(prefix='/api')
web = APIRouter(prefix='')

@web.get('/')
async def hello_world():
    return {"ping": "pong"}


@api.post('/user')
async def user_create(user: UserCreateSchema):
    try:
        await UserService.create_user(user)
        return {"message": "ok"}
    except Exception as err:
        raise HTTPException(400, detail=str(err))

@api.post('/income')
async def income_create(income: IncomeCreateSchema):
    await IncomeService.create_income(income)
    return {"message": "ok"}
