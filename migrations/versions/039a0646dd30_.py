"""empty message

Revision ID: 039a0646dd30
Revises: a174a1017c1f
Create Date: 2021-12-18 16:29:15.003256

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '039a0646dd30'
down_revision = 'a174a1017c1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('banner', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('banner', 'creat_time')
    op.create_foreign_key(None, 'cms_role_user', 'cms_user', ['cms_user_id'], ['id'])
    op.create_foreign_key(None, 'cms_role_user', 'cms_role', ['cms_role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    op.add_column('banner', sa.Column('creat_time', mysql.DATETIME(), nullable=True))
    op.drop_column('banner', 'create_time')
    # ### end Alembic commands ###
