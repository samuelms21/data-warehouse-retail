from app.extensions import db


class Store(db.Model):
    id = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(54), default=None)
    address = db.Column(db.String(54), default=None)
    phone = db.Column(db.String(54), default=None)
    
    def __repr__(self):
        return f"<Store {self.id} {self.name}>"
    