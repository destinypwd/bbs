"""empty message

Revision ID: 7637c27427e2
Revises: 01b7b8b35231
Create Date: 2021-12-18 15:42:42.108506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7637c27427e2'
down_revision = '01b7b8b35231'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banner',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('link_url', sa.String(length=255), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'cms_role_user', 'cms_user', ['cms_user_id'], ['id'])
    op.create_foreign_key(None, 'cms_role_user', 'cms_role', ['cms_role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    op.drop_table('banner')
    # ### end Alembic commands ###