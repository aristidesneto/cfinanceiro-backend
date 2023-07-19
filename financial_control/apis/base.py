from financial_control.apis import entry, user, login

from fastapi import APIRouter

router = APIRouter(prefix="/api")
router.include_router(user.router, tags=["users"])
router.include_router(entry.router, tags=["entry"])
router.include_router(login.router, tags=["login"])