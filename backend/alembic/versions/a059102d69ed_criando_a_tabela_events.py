"""Criando a tabela events

Revision ID: a059102d69ed
Revises: 08c8745f7617
Create Date: 2026-08-21 11:33:33.595579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a059102d69ed'
down_revision: Union[str, None] = '08c8745f7617'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'events',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('code', sa.String(length=20), nullable=False),
        sa.Column('client_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=150), nullable=False),
        sa.Column('event_type', sa.String(length=50), nullable=False),
        sa.Column('event_date', sa.Date(), nullable=False),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=30), nullable=False),
        sa.Column('description', sa.String(length=500), nullable=True),
        sa.Column('created_at', sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(
            ['client_id'],
            ['clients.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_index(
        op.f('ix_events_code'),
        'events',
        ['code'],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_events_code'),
        table_name='events',
    )

    op.drop_table('events')