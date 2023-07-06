"""create incomes table

Revision ID: 0778abf77b24
Revises: 45380dea57d9
Create Date: 2023-07-05 22:10:51.528729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0778abf77b24'
down_revision = '45380dea57d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'incomes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('amount', sa.Double),
        sa.Column('month', sa.String(2)),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('incomes')
