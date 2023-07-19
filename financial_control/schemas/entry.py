from typing import Optional, List
from datetime import datetime, date

from pydantic import BaseModel, PositiveFloat, ConfigDict

from financial_control.database.models.entry import EntryTypes
from financial_control.schemas.user import UserOutput

class EntryCreateSchema(BaseModel):
    category_id: int
    type: EntryTypes
    title: str
    amount: PositiveFloat
    installments: Optional[int] = None
    total_installments: Optional[int] = None
    due_date: Optional[date] = None
    payday: Optional[datetime] = None
    is_recurring: bool
    start_date: Optional[date] = None
    sequence: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deletead_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class EntryOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user: List[UserOutput]
    user_id: int
    category_id: int | None
    type: EntryTypes
    title: str
    amount: PositiveFloat
    installments: int | None
    total_installments: int | None
    due_date: date | None
    payday: datetime | None
    is_recurring: bool
    start_date: date | None
    sequence: int | None
    created_at: datetime
    updated_at: datetime | None
    deletead_at: datetime | None
