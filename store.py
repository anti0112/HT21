from storage import Storage


class Store(Storage):
    def __init__(self):
        super().__init__(capacity=100, items={})
        # self.capacity = capacity
        # self.items = items

    def add(self, name, amount_added):
        if sum(item for item in self.items.values()) < self.capacity:
            if name not in self.items.keys():
                self.items[name] = amount_added
            else:
                self.items[name] += amount_added
        else:
            print('В магазине закончилось место!')

    def remove(self, name, amount_bought):
        if sum(item for item in self.items.values()) > 0:
            self.items[name] -= amount_bought
        else:
            print('Нет предметов для удаления!')

    def get_free_space(self):
        return self.capacity - sum(item for item in self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(set([item for item in self.items.keys()]))


