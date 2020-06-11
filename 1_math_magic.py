class MyStr(str):
    def __add__(self, other):
        return f'{self}{other}'  # same type !!!
        # return list(f'{self}{other}')  # not same type -> error

    def __radd__(self, other):
        return f'{other}{self}'  # same type !!!


a = 5.5
b = '7.7'
b_new = MyStr('7.7')

# print(a + b)
# print(b + a)
print(b_new + a)
print(b_new + a + a)
# print(b_new.__add__(a))

# print(a.__add__(b_new))
# print(a + b_new + b)
# sometype + str
