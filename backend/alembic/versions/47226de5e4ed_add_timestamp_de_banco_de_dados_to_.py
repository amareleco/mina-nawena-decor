"""add timestamp de banco de dados to stock movements

Revision ID: 47226de5e4ed
Revises: af6e85836951
Create Date: 2026-08-17 15:41:23.822438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47226de5e4ed'
down_revision: Union[str, None] = 'af6e85836951'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
