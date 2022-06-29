from shop import Shop
from store import Store


def create_product_store():
    object_store = Store()
    object_shop = Shop()

    object_shop.add("Шоколадка", 2)
    object_shop.add("Сок", 2)
    object_store.add("Мандарины", 11)
    object_store.add("Печенье", 10)
    object_store.add("Доширак", 7)
    object_store.add("Пельмени", 21)

    all_items_store = object_store.get_items()
    all_items_shop = object_shop.get_items()
    print("Продукты на складе")
    print("\n".join([f"{key} - {value} шт" for key, value in all_items_store.items()]))
    print("#"*30, "\nПродукты в магазине")
    print("\n".join([f"{key} - {value} шт" for key, value in all_items_shop.items()]))


class Move:
    def __init__(self, product, amount, from_, to):
        self.product = product
        self.amount = amount
        self.from_ = from_
        self.to = to

    def find_product_in(self, place):
        try:
            place.remove(self.product, self.amount)
            print(f'\nНужное количество есть в "{self.from_}"')
        except Exception as error:
            print(f"Нужного количества нет на {self.from_} Ошибка {error}")
            return ''

    def move_product_to(self, place):
        if place.add(self.product, self.amount):
            print(f'Курьер забрал {self.amount} "{self.product}" из "{self.from_}" и везет в "{self.to}"')
            print(f'Курьер доставил {self.amount} "{self.product}" в "{self.to}"')
        else:
            raise ValueError('Недостаточно места')



