"""01_create_urls_table

Revision ID: ce1bc356a8e8
Revises: 
Create Date: 2024-10-07 11:44:06.374483

"""
import sqlalchemy as sa

from alembic import op
from typing import Sequence, Union

revision: str = '01_create_urls_table'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'urls',
        sa.Column('short_url', sa.String(length=50), nullable=False),
        sa.Column('long_url', sa.String(length=5000), nullable=False, unique=True),
        sa.PrimaryKeyConstraint('short_url')
    )


def downgrade() -> None:
    op.drop_table('urls')
