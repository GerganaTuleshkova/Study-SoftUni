class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity > len(self.storage):
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")

print(storage.get_products())
