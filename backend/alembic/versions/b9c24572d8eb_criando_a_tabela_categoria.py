"""criando a tabela categoria

Revision ID: b9c24572d8eb
Revises: 99cfbc2c0e43
Create Date: 2026-08-04 15:02:42.365701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9c24572d8eb'
down_revision: Union[str, None] = '99cfbc2c0e43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categories',

        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            'code',
            sa.String(length=20),
            nullable=False
        ),

        sa.Column(
            'name',
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            'description',
            sa.String(length=255),
            nullable=True
        ),

        sa.Column(
            'created_at',
            sa.Date(),
            nullable=False
        ),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('code'),
        sa.UniqueConstraint('name')
    )

    op.create_index(
        'ix_categories_code',
        'categories',
        ['code'],
        unique=True
    )


def downgrade() -> None:
    op.drop_index(
        'ix_categories_code',
        table_name='categories'
    )

    op.drop_table('categories')