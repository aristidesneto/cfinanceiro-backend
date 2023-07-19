from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict

class UserCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    email: str
    password: str
    avatar: Optional[str] = None
    is_admin: Optional[bool] = False
    

class UserOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    email: str
    avatar: str | None
    is_admin: bool
    status: bool
