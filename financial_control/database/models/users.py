from sqlalchemy import Boolean, Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship

from financial_control.database.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(120), nullable=True)
    is_admin = Column(Boolean(), nullable=False, default=False)
    status = Column(Boolean(), nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    # category = relationship("Category")
    entries = relationship("Entry", back_populates='user')
    
    def __repr__(self):
        return f'<User {self.name}>'