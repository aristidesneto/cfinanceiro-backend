from typing import Optional
from datetime import datetime

from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str
    created_at: Optional[datetime]