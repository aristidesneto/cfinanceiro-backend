from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from financial_control.schemas.user import UserCreateSchema, UserOutput
from financial_control.services.user import create, find_id, find_all
from financial_control.database.config import get_database
from financial_control.database.models.users import User
from financial_control.apis.login import get_current_user

router = APIRouter()

@router.post('/user', response_model=UserOutput, status_code=status.HTTP_201_CREATED)
async def user_create(user: UserCreateSchema, db: Session = Depends(get_database)):
    return await create(data=user, db=db)
    
@router.get('/users', response_model=List[UserOutput], status_code=status.HTTP_200_OK)
async def users_list(db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return await find_all(db=db)

@router.get('/user/{id}', response_model=UserOutput, status_code=status.HTTP_200_OK)
async def user_find(id: int, db: Session = Depends(get_database)):
    return await find_id(id=id, db=db)

@router.put('/user/{id}')
async def user_update(id: int):
    return {"user_updated": id}

@router.delete('/user/{id}')
async def user_delete(id: int):
    return {"user_deleteed": id}