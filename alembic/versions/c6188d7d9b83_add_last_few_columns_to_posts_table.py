"""add last few columns to posts table

Revision ID: c6188d7d9b83
Revises: 747f053c4307
Create Date: 2022-12-13 09:23:11.519886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6188d7d9b83'
down_revision = '747f053c4307'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone='True'), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_colum('posts', 'created_at')
    pass
