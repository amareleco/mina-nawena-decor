"""Add update_timestamp trigger to stock_movements

Revision ID: af91f8a923c0
Revises: 7d402b6f8d99
Create Date: 2026-08-17 16:36:02.079766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af91f8a923c0'
down_revision: Union[str, None] = '7d402b6f8d99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
from sqlalchemy import text

def upgrade():
    op.execute("""
    CREATE OR REPLACE FUNCTION update_timestamp()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """)
    
    op.execute("""
    CREATE TRIGGER stock_movements_update_timestamp
    BEFORE UPDATE ON stock_movements
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp();
    """)

def downgrade():
    op.execute("DROP TRIGGER IF EXISTS stock_movements_update_timestamp ON stock_movements")
    op.execute("DROP FUNCTION IF EXISTS update_timestamp()")
