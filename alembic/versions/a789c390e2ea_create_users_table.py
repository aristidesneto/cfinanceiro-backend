"""create users table

Revision ID: a789c390e2ea
Revises: 
Create Date: 2023-07-17 23:51:37.517373

"""
from alembic import op
import sqlalchemy as sa

from financial_control.core.security import get_password_hash


# revision identifiers, used by Alembic.
revision = 'a789c390e2ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=120), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('avatar', sa.String(length=120), nullable=True),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.Column('status', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    
    op.execute(f"INSERT INTO users (name, email, password, is_admin, status) \
        VALUES ('Administrador', 'admin@admin.com', '{get_password_hash('password')}', true, true), \
            ('Aristides Neto', 'aristides@gmail.com', '{get_password_hash('password')}', true, true), \
            ('Demo User', 'demo@gmail.com', '{get_password_hash('password')}', false, true)")


def downgrade() -> None:
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
