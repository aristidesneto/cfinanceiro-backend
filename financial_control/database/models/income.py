from sqlalchemy import Column, Double, DateTime, Integer, ForeignKey, String, func
from financial_control.database.base_model import BaseModel


class Income(BaseModel):
    __tablename__ = 'incomes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Double, nullable=False)
    month = Column(String(2), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime)
    
    def __repr__(self):
        return f'<User {self.id} ({self.user_id} {self.amount}) {self.month}>'