from typing import Optional
from datetime import date, datetime, timezone
import uuid

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class Store(db.Model):
    __tablename__ = "stores"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    name: so.Mapped[str] = so.mapped_column(sa.String(54))
    address: so.Mapped[str] = so.mapped_column(sa.String(54))
    phone: so.Mapped[str] = so.mapped_column(sa.String(54))

    transactions: so.WriteOnlyMapped['Transaction'] = so.relationship(back_populates='store')

    def __repr__(self) -> str:
        return '<Store {}>'.format(self.name)


class DateModel(db.Model):
    __tablename__ = "dates"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    full_date: so.Mapped[date] = so.mapped_column(sa.Date(), default=date.today, unique=True)
    day_name: so.Mapped[str] = so.mapped_column(sa.String(9))
    day_of_week: so.Mapped[int] = so.mapped_column(sa.Integer)
    day_of_month: so.Mapped[int] = so.mapped_column(sa.Integer)
    day_of_year: so.Mapped[int] = so.mapped_column(sa.Integer)
    month_name: so.Mapped[str] = so.mapped_column(sa.String(9))
    month_of_year: so.Mapped[int] = so.mapped_column(sa.Integer)
    year_of_date: so.Mapped[int] = so.mapped_column(sa.Integer)
    an_event: so.Mapped[bool] = so.mapped_column(sa.Boolean)
    event_name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=True, default=None)

    transactions: so.WriteOnlyMapped['Transaction'] = so.relationship(back_populates='date_model')

    def __repr__(self) -> str:
        return '<Date: {}>'.format(self.full_date.strftime('%B %d, %Y'))
    

class Product(db.Model):
    __tablename__ = "products"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    name: so.Mapped[str] = so.mapped_column(sa.String(100))
    brand: so.Mapped[str] = so.mapped_column(sa.String(100))
    category: so.Mapped[str] = so.mapped_column(sa.String(100))
    department: so.Mapped[str] = so.mapped_column(sa.String(100))

    transactions: so.WriteOnlyMapped['Transaction'] = so.relationship(back_populates='product')

    def __repr__(self) -> str:
        return '<Product {}>'.format(self.name)


# Factless Fact Table
class Promotion(db.Model):
    __tablename__ = "promotions"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    name: so.Mapped[str] = so.mapped_column(sa.String(100))
    start_date: so.Mapped[date] = so.mapped_column(sa.Date())
    end_date: so.Mapped[date] = so.mapped_column(sa.Date())

    def __repr__(self) -> str:
        return '<Promotion: {}>'.format(self.name)


class Transaction(db.Model):
    __tablename__ = "transactions"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    store_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Store.id), index=True)
    date_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(DateModel.id), index=True)
    product_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Product.id), index=True)
    promotion_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Promotion.id), index=True)

    sales_qty: so.Mapped[int] = so.mapped_column(sa.Integer) 
    unit_cost: so.Mapped[float] = so.mapped_column(sa.Float)
    regular_unit_price: so.Mapped[float] = so.mapped_column(sa.Float)
    discount_unit_price: so.Mapped[float] = so.mapped_column(sa.Float)
    net_unit_price: so.Mapped[float] = so.mapped_column(sa.Float)
    extended_discount_dollar_amount: so.Mapped[float] = so.mapped_column(sa.Float)
    extended_sales_dollar_amount: so.Mapped[float] = so.mapped_column(sa.Float)
    extended_cost_dollar_amount: so.Mapped[float] = so.mapped_column(sa.Float)
    extended_gross_profit_dollar_amount: so.Mapped[float] = so.mapped_column(sa.Float)
    created_at: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now())

    store: so.Mapped[Store] = so.relationship(back_populates='transactions')
    product: so.Mapped[Product] = so.relationship(back_populates='transactions')
    date_model: so.Mapped[DateModel] = so.relationship(back_populates='transactions')


    def __repr__(self) -> str:
        return '<Transaction {}>'.format(self.id)
    