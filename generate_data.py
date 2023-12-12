from app import app,db
from app.models import Store, Transaction, DateModel, Product
import sqlalchemy as sa
from datetime import date
app.app_context().push()

# Temporary script to insert into database
date_2 = DateModel(full_date=date(2023, 1, 2), day_name="Monday", day_of_week=2, day_of_month=2, day_of_year=2, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_3 = DateModel(full_date=date(2023, 1, 3), day_name="Tuesday", day_of_week=3, day_of_month=3, day_of_year=3, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_4 = DateModel(full_date=date(2023, 1, 4), day_name="Wednesday", day_of_week=4, day_of_month=4, day_of_year=4, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_5 = DateModel(full_date=date(2023, 1, 5), day_name="Thursday", day_of_week=5, day_of_month=5, day_of_year=5, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_6 = DateModel(full_date=date(2023, 1, 6), day_name="Friday", day_of_week=6, day_of_month=6, day_of_year=6, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_7 = DateModel(full_date=date(2023, 1, 7), day_name="Saturday", day_of_week=7, day_of_month=7, day_of_year=7, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_8 = DateModel(full_date=date(2023, 1, 8), day_name="Sunday", day_of_week=1, day_of_month=8, day_of_year=8, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_9 = DateModel(full_date=date(2023, 1, 9), day_name="Monday", day_of_week=2, day_of_month=9, day_of_year=9, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)
date_10 = DateModel(full_date=date(2023, 1, 10), day_name="Tuesday", day_of_week=3, day_of_month=10, day_of_year=10, month_name="January", month_of_year=1, year_of_date=2023, an_event=False, event_name=None)

all_dates = [date_2, date_3, date_4, date_5, date_6, date_7, date_8, date_9, date_10]
db.session.add_all(all_dates)
db.session.commit()
quit()