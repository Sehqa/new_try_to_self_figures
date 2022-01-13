import uuid
from .figure import Figure


class Circle(Figure):

    def __init__(self, name='TEST', radius=None):
        if radius is None or (radius) < 0:
            raise ValueError
        self.guid = uuid.uuid4()
        self.name = name
        self.type = 'Круг'
        self.radius = radius
        self.diameter = radius * 2
        self.square = self.calculate_square()

    def calculate_square(self):
        return 2 * 3.14 * self.radius
