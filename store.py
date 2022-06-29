from storage import Storage


class Store(Storage):
    def __init__(self, capacity=100, items={}):       
        self._capacity = capacity
        self._items = items

    def add(self, name, amount_added):
        if self.get_free_space() > amount_added:
            if name not in self._items.keys():
                self._items[name] = amount_added
                return True
            else:
                self._items[name] += amount_added
                return True
        else:
            return False
