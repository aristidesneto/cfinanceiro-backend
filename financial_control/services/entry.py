from datetime import datetime

from sqlalchemy.future import select
from sqlalchemy.orm import Session

from financial_control.database.models.entry import Entry
from financial_control.database.models.users import User


async def create_entry(data: Entry, db: Session, current_user: User):
    print(data)
    entry = Entry(
        user_id=current_user.id,
        category_id=data.category_id,
        type=data.type,
        title=data.title,
        amount=data.amount,
        installments=data.installments,
        total_installments=data.total_installments,
        due_date=data.due_date,
        payday=data.payday,
        is_recurring=data.is_recurring,
        start_date=data.start_date,
        sequence=data.sequence,
        created_at=datetime.now(),
        updated_at=data.updated_at,
        deletead_at=data.deletead_at,
    )
    db.add(entry)
    await db.flush()
    return entry
        
async def find_all(db: Session, current_user: User):
    query = await db.execute(select(Entry)
        .join_from(User, Entry)
        .where(Entry.user_id == current_user.id)
    )
    return query.scalars().all()
