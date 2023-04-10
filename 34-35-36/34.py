class Roman:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @staticmethod
    def __add__(x, y):
        return x + y

    def __add__(self, other):
        return self.x + other.x


x = Roman(1)
y = Roman(2)
print(Roman.__add__(x, y))
