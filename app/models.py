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

    def __repr__(self) -> str:
        return '<Store {}>'.format(self.name)


# Name converted to "DateModel" instead of just "Date" to avoid using python's datetime "date" keyword
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
    event_name: so.Mapped[str] = so.mapped_column(sa.String(99))

    def __repr__(self) -> str:
        return '<Date {}>'.format(self.full_date)
    

class Product(db.Model):
    __tablename__ = "products"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    name: so.Mapped[str] = so.mapped_column(sa.String(54))
    qty: so.Mapped[int] = so.mapped_column(sa.Integer)
    price: so.Mapped[int] = so.mapped_column(sa.Integer)
    init_price: so.Mapped[int] = so.mapped_column(sa.Integer)

    def __repr__(self) -> str:
        return '<Product {}'.format(self.name)


# Update Transactions table (read Kimball on retail sales)
class Transaction(db.Model):
    __tablename__ = "transactions"

    id: so.Mapped[str] = so.mapped_column(sa.String(36),primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    store_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Store.id), index=True)
    date_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(DateModel.id), index=True)
    product_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(Product.id), index=True)
    qty: so.Mapped[int] = so.mapped_column(sa.Integer)
    created_at: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now())