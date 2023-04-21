"""'Int'

Revision ID: 7283b64d79fc
Revises: 
Create Date: 2023-04-13 22:18:56.723871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7283b64d79fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('name', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('location', 'name')
    # ### end Alembic commands ###
