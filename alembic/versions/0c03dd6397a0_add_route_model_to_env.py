"""add route model to env

Revision ID: 0c03dd6397a0
Revises: 4504823eb134
Create Date: 2026-08-18 11:34:20.141189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c03dd6397a0'
down_revision: Union[str, Sequence[str], None] = '4504823eb134'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
