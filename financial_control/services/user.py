from sqlalchemy.orm import Session
from sqlalchemy.future import select

from financial_control.database.models.users import User
from financial_control.core.security import get_password_hash


async def create(data: User, db: Session):
    user = User(
        name=data.name,
        email=data.email,
        password=get_password_hash(data.password)
    )
    db.add(user)
    await db.flush()
    return user

async def find_all(db: Session):
    query = await db.execute(select(User))
    return query.scalars().all()

async def find_id(id: int, db: Session):
    query = await db.execute(select(User).filter(User.id == id))
    return query.scalars().first()

async def get_user(email: str, db: Session):
    query = await db.execute(select(User).filter(User.email == email))
    return query.scalars().first()