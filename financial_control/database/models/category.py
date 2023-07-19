from sqlalchemy import Boolean, Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import relationship

from financial_control.database.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(120))
    status = Column(Boolean(), default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime)
    
    # entry = relationship("Entry", back_populates='category')
    # entries = relationship("Entry", back_populates='category')
    user = relationship("User")
    
    def __repr__(self):
        return f'<Category {self.name}>'