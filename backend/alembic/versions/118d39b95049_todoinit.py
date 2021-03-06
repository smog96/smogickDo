"""TodoInit

Revision ID: 118d39b95049
Revises: 8ab2fa469895
Create Date: 2022-04-04 11:26:05.003163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '118d39b95049'
down_revision = '8ab2fa469895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('deadline_date', sa.Date(), nullable=True),
    sa.Column('is_complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='My ToDo list'
    )
    op.create_index(op.f('ix_todos_id'), 'todos', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todos_id'), table_name='todos')
    op.drop_table('todos')
    # ### end Alembic commands ###
