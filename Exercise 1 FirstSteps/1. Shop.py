class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = list(items)

    def get_items_count(self):
        return len(self.items)


shop = Shop("Product Shop", [1, 2, 3])
print(shop.get_items_count())
