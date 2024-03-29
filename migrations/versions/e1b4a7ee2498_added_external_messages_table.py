"""Added external messages table

Revision ID: e1b4a7ee2498
Revises: bd640d969f45
Create Date: 2023-05-09 19:31:35.183935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1b4a7ee2498'
down_revision = 'bd640d969f45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extern__messages',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('tags', sa.String(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('extern__messages')
    # ### end Alembic commands ###
