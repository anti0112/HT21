from storage import Storage


class Store(Storage):
    def __init__(self, capacity=100, items={}):       
        self._capacity = capacity
        self._items = items

    def add(self, name, amount_added):
        if sum(item for item in self._items.values()) < self._capacity:
            if name not in self._items.keys():
                self._items[name] = amount_added
            else:
                self._items[name] += amount_added
        else:
            print('В магазине закончилось место!')
