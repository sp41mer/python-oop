class ShopItem:
    def __init__(self, price):
        self._price = price


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
