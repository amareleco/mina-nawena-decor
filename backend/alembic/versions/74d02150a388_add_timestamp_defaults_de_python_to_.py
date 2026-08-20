"""add timestamp defaults de python to stock movements

Revision ID: 74d02150a388
Revises: 38ddb3d5f188
Create Date: 2026-08-17 12:56:54.688708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74d02150a388'
down_revision: Union[str, None] = '38ddb3d5f188'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('stock_movements', 'created_at',
               existing_type=sa.DateTime(),
               server_default=sa.func.now())
    op.alter_column('stock_movements', 'updated_at',
               existing_type=sa.DateTime(),
               server_default=sa.func.now())

def downgrade():
    op.alter_column('stock_movements', 'created_at',
               existing_type=sa.DateTime(),
               server_default=None)
    op.alter_column('stock_movements', 'updated_at',
               existing_type=sa.DateTime(),
               server_default=None)