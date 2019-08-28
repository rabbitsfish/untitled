class Money(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if isinstance(value, int):
            self.__num = value
        else:
            print('it is not a dit')

