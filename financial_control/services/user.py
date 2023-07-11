from financial_control.models.users import User
from financial_control.database.config import async_session

from datetime import datetime

class UserService():
    async def create_user(data: User):
        async with async_session() as session:
            session.add(User(
                name=data.name,
                email=data.email,
                password=data.password
            ))
            await session.commit()