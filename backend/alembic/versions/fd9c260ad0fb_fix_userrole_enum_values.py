"""fix userrole enum values

Revision ID: fd9c260ad0fb
Revises: 6192f396f0a5
Create Date: 2026-08-17 22:41:56.948013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd9c260ad0fb'
down_revision: Union[str, None] = '6192f396f0a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass