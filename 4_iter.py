class ShopItem:
    def __init__(self, price):
        self._price = price

    def __str__(self):
        return f'{self.__class__.__name__}: {self._price}'


class Notebook(ShopItem):
    pass


class Bath(ShopItem):
    pass


class Basket:
    def __init__(self):
        self._items = {}

    def __setitem__(self, key, value):
        try:
            value._price
            self._items[key] = value
        except Exception as e:
            raise ValueError(f'can\'t add to basket {value}: {e}')

    def __getitem__(self, item):
        return self._items.get(item)

    def __iter__(self):
        # return 'hello'
        return (el for el in self._items.values())

