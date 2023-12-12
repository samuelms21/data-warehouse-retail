from app.extensions import db
import uuid


class StoreModel(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(54), default=None)
    address = db.Column(db.String(54), default=None)
    phone = db.Column(db.String(54), default=None)

    def __repr__(self):
        return f"<Store ID: {self.id}, Name: {self.name}>"