from financial_control.models.income import Income
from financial_control.database.config import async_session

from datetime import datetime

class IncomeService():
    async def create_income(data: Income):
        async with async_session() as session:
            session.add(Income(
                user_id=1, # Pegar ID do usuário logado
                amount=data.amount,
                month=data.month,
                created_at=datetime.now()
            ))
            await session.commit()