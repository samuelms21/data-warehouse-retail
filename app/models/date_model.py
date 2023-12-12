from app.extensions import db

class DateModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_date = db.Column(db.Date, default=None)
    day_name = db.Column(db.String(9), default=None)
    day_of_week = db.Column(db.Integer, default=None)
    day_of_month = db.Column(db.Integer, default=None)
    day_of_year = db.Column(db.Integer, default=None)
    month_name = db.Column(db.String(9), default=None)
    month_of_year = db.Column(db.Integer, default=None)
    year_of_date = db.Column(db.Integer, default=None)
    an_event = db.Column(db.Boolean, default=None)

    def __repr__(self):
        return f"<DateModel {self.id} {self.full_date}>"