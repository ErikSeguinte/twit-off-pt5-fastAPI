"""empty message

Revision ID: 4ae1f57993b2
Revises: 4cc0adbb74fe
Create Date: 2020-06-09 10:20:42.473832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae1f57993b2'
down_revision = '4cc0adbb74fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('api_key', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###
