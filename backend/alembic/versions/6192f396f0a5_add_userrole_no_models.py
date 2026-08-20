"""ADD: UserRole no models

Revision ID: 6192f396f0a5
Revises: 80b080aad7c9
Create Date: 2026-08-17 21:05:31.057779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6192f396f0a5'
down_revision: Union[str, None] = '80b080aad7c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
