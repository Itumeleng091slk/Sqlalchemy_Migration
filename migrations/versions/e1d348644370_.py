"""empty message

Revision ID: e1d348644370
Revises: 
Create Date: 2020-04-07 08:39:36.129780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1d348644370'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recruit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('surname', sa.String(length=20), nullable=True),
    sa.Column('chat_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('github_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('id_number', sa.NUMERIC(precision=15), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recruit')
    op.drop_table('user')
    # ### end Alembic commands ###
