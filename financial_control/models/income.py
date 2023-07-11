from sqlalchemy import Column, Integer, DECIMAL, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    amount = Column(DECIMAL)
    month = Column(String)