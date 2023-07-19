from fastapi import APIRouter, Depends, HTTPException, status, encoders
from sqlalchemy.orm import Session
from typing import List

from financial_control.database.models.users import User
from financial_control.schemas.entry import EntryCreateSchema, EntryOutput
from financial_control.services.entry import create_entry, find_all
from financial_control.database.config import get_database
from financial_control.apis.login import get_current_user

router = APIRouter()

@router.post('/entries')
async def entry_create(entry: EntryCreateSchema, db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    return await create_entry(data=entry, db=db, current_user=current_user)


@router.get('/entries', status_code=status.HTTP_200_OK)
async def entries_list(db: Session = Depends(get_database), current_user: User = Depends(get_current_user)):
    entries = await find_all(db=db, current_user=current_user)
    
    # print(entries.user.name)
    # new_entries = []
    for entry in entries:
        print(entry)
    
    # print(EntryOutput(entries))
    # print(EntryOutput(entries))
    # print(encoders.jsonable_encoder(entries))
    # entry_decode = List[EntryOutput(**encoders.jsonable_encoder(entries)).model_dump()]
    # print(entry_decode)
    return entries