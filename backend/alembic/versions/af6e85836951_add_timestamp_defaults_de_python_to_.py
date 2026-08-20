"""add timestamp defaults de python to stock movements

Revision ID: af6e85836951
Revises: c49de6a6b415
Create Date: 2026-08-17 13:17:05.850486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af6e85836951'
down_revision: Union[str, None] = 'c49de6a6b415'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
