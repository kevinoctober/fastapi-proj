"""add foreign-key to posts table

Revision ID: 747f053c4307
Revises: 8c2e208f1be6
Create Date: 2022-12-13 09:14:54.335157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '747f053c4307'
down_revision = '8c2e208f1be6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')

    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
