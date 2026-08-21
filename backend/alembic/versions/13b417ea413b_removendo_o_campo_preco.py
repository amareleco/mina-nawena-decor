"""Removendo o campo preco

Revision ID: 13b417ea413b
Revises: 6cbde48d9501
Create Date: ...

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '13b417ea413b'
down_revision: Union[str, None] = '6cadd4388f75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass