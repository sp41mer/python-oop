class ShopItem:
    def __init__(self, price):
        self._price = price

    def __str__(self):
        return f'{self.__class__.__name__}: {self._price}'


class Notebook(ShopItem):
    pass


class Bath(ShopItem):
    pass


class BasketIterator:
    def __init__(self, vals, idx=0):
        self.idx = idx
        self.vals = list(vals)

    def __next__(self):
        if self.idx < len(self.vals):
            self.idx += 1
            return self.vals[self.idx - 1]
        else:
            raise StopIteration


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
        # return 'some object having __next__'
        # return self
        return BasketIterator(self._items.values())
