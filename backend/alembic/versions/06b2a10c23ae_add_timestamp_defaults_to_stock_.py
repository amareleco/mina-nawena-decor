"""add timestamp defaults to stock movements

Revision ID: 06b2a10c23ae
Revises: 7a12a746d4fa
Create Date: 2026-08-17 12:54:48.070775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06b2a10c23ae'
down_revision: Union[str, None] = '7a12a746d4fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
