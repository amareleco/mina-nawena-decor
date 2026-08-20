"""fix userrole enum values

Revision ID: fd9c260ad0fb
Revises: 6192f396f0a5
Create Date: 2026-08-17 22:41:56.948013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd9c260ad0fb'
down_revision: Union[str, None] = '6192f396f0a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Converter valores existentes para minúsculas
    op.execute("UPDATE users SET role = LOWER(role)")
    
    # Criar o tipo ENUM (se não existir)
    op.execute("DROP TYPE IF EXISTS userrole CASCADE")
    op.execute("CREATE TYPE userrole AS ENUM ('admin', 'manager', 'employee')")
    
    # Converter a coluna
    op.alter_column('users', 'role',
        existing_type=sa.VARCHAR(length=50),
        type_=sa.Enum('admin', 'manager', 'employee', name='userrole', native_enum=True),
        existing_nullable=False,
        postgresql_using='role::userrole')


def downgrade() -> None:
    op.alter_column('users', 'role',
        existing_type=sa.Enum('admin', 'manager', 'employee', name='userrole', native_enum=True),
        type_=sa.VARCHAR(length=50),
        existing_nullable=False)
    
    op.execute("DROP TYPE IF EXISTS userrole CASCADE")
