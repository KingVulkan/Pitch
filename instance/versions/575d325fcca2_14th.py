"""14th

Revision ID: 575d325fcca2
Revises: 2425b6924b1c
Create Date: 2018-09-10 10:37:35.202719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575d325fcca2'
down_revision = '2425b6924b1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorys')
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    op.drop_constraint('pitches_category_id_fkey', 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'category_id')
    op.drop_constraint('users_category_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_category_id_fkey', 'users', 'categorys', ['category_id'], ['id'])
    op.add_column('pitches', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitches_category_id_fkey', 'pitches', 'categorys', ['category_id'], ['id'])
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.drop_column('pitches', 'category')
    op.create_table('categorys',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='categorys_pkey')
    )
    # ### end Alembic commands ###
