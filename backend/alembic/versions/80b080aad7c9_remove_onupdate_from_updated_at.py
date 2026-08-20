"""Remove onupdate from updated_at

Revision ID: 80b080aad7c9
Revises: af91f8a923c0
Create Date: 2026-08-17 17:07:23.720085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80b080aad7c9'
down_revision: Union[str, None] = 'af91f8a923c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('stock_movements', 'updated_at',
               existing_type=sa.DateTime(),
               server_onupdate=None)

def downgrade():
    op.alter_column('stock_movements', 'updated_at',
               existing_type=sa.DateTime(),
               server_onupdate=sa.func.now())
