from sqlalchemy import Boolean, Column, Double, DateTime, Date, Enum, Integer, ForeignKey, String, func
from sqlalchemy.orm import relationship
import enum

from financial_control.database.base_model import BaseModel

class EntryTypes(enum.Enum):
    expense='expense'
    income='income'

class Entry(BaseModel):
    __tablename__ = 'entries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    type = Column(Enum(EntryTypes), default='expense', nullable=False)
    title = Column(String(200), nullable=False, comment='Title of the entry')
    amount = Column(Double, nullable=False)
    installments = Column(Integer, nullable=True, comment='Number of installments')
    total_installments = Column(Integer, nullable=True, comment='Total number of installments')
    due_date = Column(Date, nullable=True)
    payday = Column(Date, nullable=True)
    is_recurring = Column(Boolean(), default=False, nullable=True, comment='If recurring is expense')
    start_date = Column(Date, nullable=True, comment='Expense start date and/or revenue reference')
    sequence = Column(Integer, nullable=True, comment='Grouping of recurring installments')
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, nullable=True)
    deletead_at = Column(DateTime, nullable=True)
    
    # category = relationship("Category", back_populates='entry')
    user = relationship("User", back_populates='entries')

    def __repr__(self):
        return f'<Title: {self.title} - Amount: {self.amount}>'