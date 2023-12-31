"""empty message

Revision ID: 11a1352d9e59
Revises: e263749a0bff
Create Date: 2023-12-12 14:07:50.220881

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11a1352d9e59'
down_revision = 'e263749a0bff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dates', schema=None) as batch_op:
        batch_op.alter_column('event_name',
               existing_type=mysql.VARCHAR(length=99),
               type_=sa.String(length=100),
               existing_nullable=False)

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('category', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('departmen', sa.String(length=100), nullable=False))
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=54),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.drop_column('qty')
        batch_op.drop_column('init_price')
        batch_op.drop_column('price')

    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sales_qty', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('unit_cost', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('regular_unit_price', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('discount_unit_price', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('net_unit_price', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('extended_discount_dollar_amount', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('extended_sales_dollar_amount', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('extended_cost_dollar_amount', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('extended_gross_profit_dollar_amount', sa.Float(), nullable=False))
        batch_op.drop_column('qty')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qty', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.drop_column('extended_gross_profit_dollar_amount')
        batch_op.drop_column('extended_cost_dollar_amount')
        batch_op.drop_column('extended_sales_dollar_amount')
        batch_op.drop_column('extended_discount_dollar_amount')
        batch_op.drop_column('net_unit_price')
        batch_op.drop_column('discount_unit_price')
        batch_op.drop_column('regular_unit_price')
        batch_op.drop_column('unit_cost')
        batch_op.drop_column('sales_qty')

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('init_price', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('qty', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=54),
               existing_nullable=False)
        batch_op.drop_column('departmen')
        batch_op.drop_column('category')
        batch_op.drop_column('brand')

    with op.batch_alter_table('dates', schema=None) as batch_op:
        batch_op.alter_column('event_name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=99),
               existing_nullable=False)

    # ### end Alembic commands ###
