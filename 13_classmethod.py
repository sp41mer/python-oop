class Currency:
    def __init__(self, rate):
        self.rate = rate


class ShopItem:
    items = 0

    def __init__(self, price):
        self._price = price

    def __add__(self, other):
        return ShopItem(self._price + other._price)

    def __str__(self):
        return f'{self.__class__.__name__}: {self._price}'

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print(f'__getattr__: {item}')
        return 'stub'

    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        return amount * from_currency.rate / to_currency.rate

    @classmethod
    def create_from_currency(cls, amount, from_currency, to_currency):
        return cls(
            cls.convert_currency(amount, from_currency, to_currency)
        )

    @classmethod
    def create_and_count(cls, price):
        cls.items += 1
        return cls(price)


class Notebook(ShopItem):
    pass


class Bath(ShopItem):
    pass
