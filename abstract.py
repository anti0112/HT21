from abc import ABC, abstractmethod


class Abstract(ABC):

    @property
    @abstractmethod
    def remove(self):
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
