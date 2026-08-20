"""add timestamp defaults de python to stock movements

Revision ID: c49de6a6b415
Revises: e37f4dad3944
Create Date: 2026-08-17 13:13:54.683757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c49de6a6b415'
down_revision: Union[str, None] = 'e37f4dad3944'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
