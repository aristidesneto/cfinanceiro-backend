from typing import Optional
from datetime import datetime

from pydantic import BaseModel, PositiveFloat

class IncomeCreateSchema(BaseModel):
    amount: PositiveFloat
    month: str