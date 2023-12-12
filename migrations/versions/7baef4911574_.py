"""empty message

Revision ID: 7baef4911574
Revises: 53278b3e5e6d
Create Date: 2023-12-12 12:22:27.982851

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7baef4911574'
down_revision = '53278b3e5e6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('date_model',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('full_date', sa.Date(), nullable=False),
    sa.Column('day_name', sa.String(length=9), nullable=False),
    sa.Column('day_of_week', sa.Integer(), nullable=False),
    sa.Column('day_of_month', sa.Integer(), nullable=False),
    sa.Column('day_of_year', sa.Integer(), nullable=False),
    sa.Column('month_name', sa.String(length=9), nullable=False),
    sa.Column('month_of_year', sa.Integer(), nullable=False),
    sa.Column('year_of_date', sa.Integer(), nullable=False),
    sa.Column('an_event', sa.Boolean(), nullable=False),
    sa.Column('event_name', sa.String(length=99), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('full_date'),
    sa.UniqueConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=54), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('init_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    with op.batch_alter_table('store', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.CHAR(length=32),
               type_=sa.String(length=36),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('store', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=36),
               type_=mysql.CHAR(length=32),
               existing_nullable=False)

    op.drop_table('product')
    op.drop_table('date_model')
    # ### end Alembic commands ###