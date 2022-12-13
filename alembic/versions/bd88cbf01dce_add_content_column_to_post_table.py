"""add content column to post table

Revision ID: bd88cbf01dce
Revises: 6f6409181c91
Create Date: 2022-12-13 08:54:39.475165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd88cbf01dce'
down_revision = '6f6409181c91'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
