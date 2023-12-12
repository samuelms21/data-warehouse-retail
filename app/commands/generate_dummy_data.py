from app.extensions import db
from app.models.store_model import StoreModel

def generate_dummy_data():
    # Create some dummy data
    store1 = StoreModel(name="Store 1", address="Address 1", phone="Phone 1")
    store2 = StoreModel(name="Store 2", address="Address 2", phone="Phone 2")

    # Add the dummy data to the session
    db.session.add(store1)
    db.session.add(store2)

    # Commit the session to save the data
    db.session.commit()