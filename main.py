from utils import create_product_store, Move
from store import Store
from shop import Shop


def main():
    all_items_store = store.get_items()
    all_items_shop = shop.get_items()

    product = input('Что хотите доставить: ')

    if product in all_items_store or all_items_shop:
        amount = int(input('Введите количество: '))
        from_ = input('Откуда забирать: ')
        print("Доступные варианты: магазин, склад")
        to = input('Куда везем: ')

    else:
        return print("Такого продукта нет")

    move = Move(product, amount, from_, to)
    if to == 'магазин':
        move.find_product_in(store)
        move.move_product_to(shop)
    elif to == 'склад':
        move.find_product_in(shop)
        move.move_product_to(store)
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
