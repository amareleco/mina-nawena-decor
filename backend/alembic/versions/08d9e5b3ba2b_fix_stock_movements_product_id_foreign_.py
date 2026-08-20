"""fix stock_movements product_id foreign key cascade

Revision ID: 08d9e5b3ba2b
Revises: cdf8d36dc1ec
Create Date: 2026-08-18 02:57:37.144738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08d9e5b3ba2b'
down_revision: Union[str, None] = 'cdf8d36dc1ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Dropar FK existente
    op.execute("ALTER TABLE stock_movements DROP CONSTRAINT IF EXISTS stock_movements_product_id_fkey")
    
    # 2. Converter VARCHAR para INTEGER
    op.alter_column('stock_movements', 'product_id',
        existing_type=sa.String(),
        type_=sa.Integer(),
        existing_nullable=False,
        postgresql_using='product_id::integer')
    
    # 3. Criar FK com CASCADE
    op.create_foreign_key(
        'stock_movements_product_id_fkey',
        'stock_movements', 'products',
        ['product_id'], ['id'],
        ondelete='CASCADE'
    )

def downgrade() -> None:
    op.drop_constraint('stock_movements_product_id_fkey', 'stock_movements', type_='foreignkey')
    
    op.alter_column('stock_movements', 'product_id',
        existing_type=sa.Integer(),
        type_=sa.String(),
        existing_nullable=False)