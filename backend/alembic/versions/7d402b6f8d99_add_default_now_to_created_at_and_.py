"""Add DEFAULT now() to created_at and updated_at

Revision ID: 7d402b6f8d99
Revises: 8bab00a43bf0
Create Date: 2026-08-17 16:17:18.571975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d402b6f8d99'
down_revision: Union[str, None] = '8bab00a43bf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
