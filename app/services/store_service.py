from app.models.store_model import Store


class StoreService:
    @staticmethod
    def get_all_stores():
        return Store.query.all()