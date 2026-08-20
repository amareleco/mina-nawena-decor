"""add timestamp defaults to stock movements

Revision ID: 38ddb3d5f188
Revises: 06b2a10c23ae
Create Date: 2026-08-17 12:55:08.866715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38ddb3d5f188'
down_revision: Union[str, None] = '06b2a10c23ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
