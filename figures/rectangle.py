import uuid
from .figure import Figure


class Rectangle(Figure):
    def __init__(self, name='TEST', first_side=None, second_side=None):
        if (first_side is None) or (second_side is None):
            raise ValueError
        elif (first_side < 0) or (second_side < 0):
            raise ValueError
        else:
            self.guid = uuid.uuid4()
            self.name = name
            self.type = 'Прямоугольник'
            self.first_side = first_side
            self.second_side = second_side
            self.square = self.calculate_square()

