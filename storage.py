from abc import ABC, abstractmethod

import self as self


class Storage(ABC):
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    @property
    @abstractmethod
    def add(self, name, count):
        pass

    @property
    @abstractmethod
    def remove(self, name, count):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass
