"""add timestamp defaults to stock movements

Revision ID: 7a12a746d4fa
Revises: 0878019b4f78
Create Date: 2026-08-17 12:54:42.962541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a12a746d4fa'
down_revision: Union[str, None] = '0878019b4f78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
