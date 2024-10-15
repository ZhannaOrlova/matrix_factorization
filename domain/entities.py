class User:
    def __init__(self, user_id: int):
        self.user_id = user_id

class Item:
    def __init__(self, item_id: int):
        self.item_id = item_id

class Rating:
    def __init__(self, user: User, item: Item, rating: float):
        self.user = user
        self.item = item
        self.rating = rating
