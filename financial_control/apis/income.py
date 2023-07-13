from fastapi import APIRouter, HTTPException

from financial_control.schemas.income import IncomeCreateSchema
from financial_control.services.income import IncomeService

router = APIRouter()

@router.post('/')
async def income_create(income: IncomeCreateSchema):
    await IncomeService.create_income(income)
    return {"message": "ok"}