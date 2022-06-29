from store import Store


def create_product_store():
    object_store = Store()
    object_store.add("Мандарины", 11)
    object_store.add("Печенье", 10)
    object_store.add("Доширак", 7)
    object_store.add("Пельмени", 15)
    all_items = object_store.get_items()
    print("\n".join([f"{key} - {value} шт" for key, value in all_items.items()]))
    return all_items
    
