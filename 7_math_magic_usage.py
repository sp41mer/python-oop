class ShopItem:
    def __init__(self, price):
        self._price = price

    def __add__(self, other):
        return ShopItem(self._price + other._price)

    def __str__(self):
        return f'{self.__class__.__name__}: {self._price}'


class Notebook(ShopItem):
    pass


class Bath(ShopItem):
    pass


class Basket:
    def __init__(self):
        self._items = {}
        self._idx = 0
        self._iter_items = []

    def __setitem__(self, key, value):
        try:
            value._price
            self._items[key] = value
        except Exception as e:
            raise ValueError(f'can\'t add to basket {value}: {e}')

    def __getitem__(self, item):
        return self._items.get(item)

    def __iter__(self):
        if not self._iter_items:
            self._iter_items = tuple(self._items.values())
        self._idx = 0
        return self

    def __next__(self):
        if self._idx < len(self._iter_items):
            self._idx += 1
            return self._iter_items[self._idx - 1]
        else:
            raise StopIteration
