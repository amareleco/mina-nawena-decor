"""Add DEFAULT now() to created_at and updated_at

Revision ID: 8bab00a43bf0
Revises: 47226de5e4ed
Create Date: 2026-08-17 16:15:00.702704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bab00a43bf0'
down_revision: Union[str, None] = '47226de5e4ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
