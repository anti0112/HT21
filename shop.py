from storage import Storage


class Shop(Storage):
    def __init__(self, capacity=20, _items={}, unique=5):       
        self._capacity = capacity
        self._items = _items
        self.unique = unique

    def add(self, name, amount_added):
        if self.get_free_space() > amount_added:
            if name not in self._items.keys() and len(self._items) <= self.unique:
                self._items[name] = amount_added
                return True
            else:
                self._items[name] += amount_added
                return True
        else:
            return False

