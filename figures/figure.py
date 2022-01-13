from abc import ABC


class Figure(ABC):

    def __init__(self):
        self.name = 'name'
        self.type = 'type'
        self.square = self.calculate_square()

    def calculate_square(self):
        square = 0
        for i in list(name for name in self.__dict__ if name.endswith('_side')):
            square = square + self.__dict__[i]
        return square
