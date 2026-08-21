"""criando a tabela product

Revision ID: 179d051a76c8
Revises: b9c24572d8eb
Create Date: 2026-08-04 15:42:52.546899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '179d051a76c8'
down_revision: Union[str, None] = 'b9c24572d8eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('code', sa.String(length=20), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('minimum_stock', sa.Integer(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.Date(), nullable=False),

        sa.ForeignKeyConstraint(
            ['category_id'],
            ['categories.id']
        ),

        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(
        'ix_products_code',
        'products',
        ['code'],
        unique=True
    )


def downgrade() -> None:
    op.drop_index(
        'ix_products_code',
        table_name='products'
    )

    op.drop_table('products')