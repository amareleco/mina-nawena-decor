"""criar de tabelas users

Revision ID: 99cfbc2c0e43
Revises: e8f70ea9557b
Create Date: 2026-08-04 14:33:09.871234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '99cfbc2c0e43'
down_revision: Union[str, None] = 'e8f70ea9557b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',

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
            'email',
            sa.String(length=150),
            nullable=False
        ),

        sa.Column(
            'password',
            sa.String(length=255),
            nullable=False
        ),

        sa.Column(
            'role',
            sa.Enum(
                'admin',
                'manager',
                'employee',
                name='userrole'
            ),
            nullable=False
        ),

        sa.Column(
            'is_active',
            sa.Boolean(),
            nullable=False,
            server_default=sa.text('true')
        ),

        sa.Column(
            'created_at',
            sa.Date(),
            nullable=False,
            server_default=sa.text('CURRENT_DATE')
        ),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('code'),
        sa.UniqueConstraint('email')
    )

    op.create_index(
        op.f('ix_users_code'),
        'users',
        ['code'],
        unique=True
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_users_code'),
        table_name='users'
    )

    op.drop_table('users')

    sa.Enum(
        'admin',
        'manager',
        'employee',
        name='userrole'
    ).drop(op.get_bind(), checkfirst=True)