"""empty message

Revision ID: cd234f795e11
Revises: fbb45d191fa7
Create Date: 2021-12-21 13:38:05.146219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd234f795e11'
down_revision = 'fbb45d191fa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'cms_role_user', 'cms_role', ['cms_role_id'], ['id'])
    op.create_foreign_key(None, 'cms_role_user', 'cms_user', ['cms_user_id'], ['id'])
    op.create_foreign_key(None, 'post', 'board', ['board_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    # ### end Alembic commands ###
