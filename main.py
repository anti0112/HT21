from utils import create_product_store
from store import Store
from shop import Shop


def main():
    all_items_store = store.get_items()
    all_items_shop = shop.get_items()

    product = input('Что хотите доставить: ')

    if product in all_items_store or all_items_shop:
        amount = int(input('Введите количество: '))
        print("Доступные варианты: магазин")
        to = input('Куда везем: ')
        from_ = input('Откуда: ')
    else:
        return print("Такого продукта нет")

    if to == 'магазин':
        try:
            store.remove(product, amount)
            print(f'\nНужное количество есть в "{from_}"')
        except Exception as error:
            print(f"Нужного количества нет на {from_} Ошибка {error}")
            return ''

        try:
            shop.add(product, amount)
            print(f'Курьер забрал {amount} "{product}" из "{from_}" и везет в "{to}"')
            print(f'Курьер доставил {amount} "{product}" в "{to}"')
        except Exception as error:
            print(error)
            return ''
    else:
        return print(f'Проверьте правильность написания места доставки')

    # Выводим кол-во товаров на складе и в магазине
    print(f'\nВ "{from_}" хранится:')
    for k, v in all_items_store.items():
        print(f' - {k}: {v}')
    print(f'Свободного места осталось: {store.get_free_space()}')
    print(f'\nВ "{to}" хранится:')
    for k, v in all_items_shop.items():
        print(f' - {k}: {v}')
    print(f'Свободного места осталось: {shop.get_free_space()}')


if __name__ == '__main__':
    create_product_store()
    store = Store()
    shop = Shop()
    while shop.get_free_space() > 0:
        print("#" * 30)
        main()
    print("Закончилось место")
