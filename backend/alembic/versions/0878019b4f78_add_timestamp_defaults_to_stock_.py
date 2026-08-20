"""add timestamp defaults to stock movements

Revision ID: 0878019b4f78
Revises: 8c59f966d620
Create Date: 2026-08-17 12:51:54.029377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0878019b4f78'
down_revision: Union[str, None] = '8c59f966d620'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
