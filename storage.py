class Storage():
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    def remove(self, title, amount):
        if sum(self._items.values()) > 0 and self._items[title] - amount > 0:
            self._items[title] -= amount
        elif self._items[title] - amount == 0:
            del self._items[title]
        else:
            raise

    def get_free_space(self):
        return self._capacity - sum(item for item in self._items.values())

    def get_items(self) -> dict:
        return self._items

    def get_unique_items_count(self):
        return len(set([item for item in self._items.keys()]))
        