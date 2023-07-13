from sqlalchemy import Boolean, Column, DateTime, String, Integer, func
from financial_control.database.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean(), nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime)

    def __repr__(self):
        return f'<User {self.id} ({self.name} {self.email}) {self.password}>'