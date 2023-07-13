from financial_control.apis import user, income, login

from fastapi import APIRouter

router = APIRouter(prefix="/api")
router.include_router(user.router, tags=["users"])
router.include_router(income.router, tags=["incomes"])
router.include_router(login.router, tags=["login"])