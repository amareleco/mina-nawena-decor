"""add timestamp defaults de python to stock movements

Revision ID: e37f4dad3944
Revises: 74d02150a388
Create Date: 2026-08-17 13:13:43.660595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e37f4dad3944'
down_revision: Union[str, None] = '74d02150a388'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
