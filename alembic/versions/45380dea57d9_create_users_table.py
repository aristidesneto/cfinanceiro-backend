"""create users table

Revision ID: 45380dea57d9
Revises: 
Create Date: 2023-07-03 23:53:09.758146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45380dea57d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(120), nullable=False),
        sa.Column('email', sa.String(120), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('users')
