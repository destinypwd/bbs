"""empty message

Revision ID: 5c5ba892b5d3
Revises: 8e0693ed4dd7
Create Date: 2021-12-07 19:08:04.669656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c5ba892b5d3'
down_revision = '8e0693ed4dd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=False),
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cms_role_user',
    sa.Column('cms_role_id', sa.Integer(), nullable=False),
    sa.Column('cms_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cms_role_id'], ['cms_role.id'], ),
    sa.ForeignKeyConstraint(['cms_user_id'], ['cms_user.id'], ),
    sa.PrimaryKeyConstraint('cms_role_id', 'cms_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cms_role_user')
    op.drop_table('cms_role')
    # ### end Alembic commands ###