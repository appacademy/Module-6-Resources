"""change image_url to url on posts

Revision ID: 9ee31abb7e74
Revises: 10d3670757d6
Create Date: 2023-07-20 11:53:44.962482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ee31abb7e74'
down_revision = '10d3670757d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=255), nullable=False))
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('image')

    # ### end Alembic commands ###