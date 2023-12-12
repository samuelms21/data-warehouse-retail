import random
import string
from app.models.store_model import Store

def generate_dummy_data(db):
    # Generate and insert dummy data
    for _ in range(10):
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        address = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))
        phone = ''.join(random.choices(string.digits, k=10))

        # Validate and truncate values if necessary
        name = name[:Store.name.property.columns[0].type.length]
        address = address[:Store.address.property.columns[0].type.length]
        phone = phone[:Store.phone.property.columns[0].type.length]

        store = Store(name=name, address=address, phone=phone)
        db.session.add(store)
    
    db.session.commit()
