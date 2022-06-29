from storage import Storage


class Shop(Storage):
    def __init__(self, capacity=20, _items={}, unique=5):       
        self._capacity = capacity
        self._items = _items
        self.unique = unique

    def add(self, name, amount_added):
        if sum(self._items.values()) < self._capacity:
            if name not in self._items.keys() and len(self._items) <= self.unique:
                self._items[name] = amount_added
            else:
                self._items[name] += amount_added
        else:
            print('В магазине закончилось место!')

