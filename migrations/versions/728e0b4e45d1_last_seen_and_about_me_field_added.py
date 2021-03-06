"""last seen and about me field added

Revision ID: 728e0b4e45d1
Revises: 
Create Date: 2018-09-18 20:45:22.616000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '728e0b4e45d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
