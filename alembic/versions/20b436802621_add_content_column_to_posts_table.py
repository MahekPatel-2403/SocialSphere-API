"""add content column to posts table

Revision ID: 20b436802621
Revises: ee4712f9639c
Create Date: 2026-08-16 23:22:26.569493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20b436802621'
down_revision: Union[str, Sequence[str], None] = 'ee4712f9639c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
