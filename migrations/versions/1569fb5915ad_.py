"""empty message

Revision ID: 1569fb5915ad
Revises: 26b8a1438602
Create Date: 2016-07-24 10:12:14.625565

"""

# revision identifiers, used by Alembic.
revision = '1569fb5915ad'
down_revision = '26b8a1438602'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('trash_date', sa.DateTime(), nullable=True))
    op.add_column('session_version', sa.Column('trash_date', sa.DateTime(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('trash_date', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'trash_date')
    op.drop_column('session_version', 'trash_date')
    op.drop_column('session', 'trash_date')
    ### end Alembic commands ###
