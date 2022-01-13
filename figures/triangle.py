import uuid
import math
from .figure import Figure


class Triangle(Figure):

    def __init__(self, name='TEST', first_side=None, second_side=None, third_side=None, first_corner=None,
                 second_corner=None, third_corner=None):
        self.name = name
        self.type = 'Треугольник'
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        self.first_corner = first_corner
        self.second_corner = second_corner
        self.third_corner = third_corner
        if (first_side is None) and (second_side is None) and (third_side is None):
            raise ValueError
        elif (first_side < 0) or (second_side < 0) or (third_side < 0):
            raise ValueError
        elif (first_side > 0) and (second_side > 0) and (third_side > 0):
            self.square = self.calculate_square()
        else:
            self.square = self.calculate_square_wtih_two_side()


    def calculate_square(self):
        return math.sqrt(((self.first_side + self.second_side + self.third_side) / 2) * (
                ((self.first_side + self.second_side + self.third_side) / 2 - self.first_side) * (
                (self.first_side + self.second_side + self.third_side) / 2 - self.second_side) * (
                        (self.first_side + self.second_side + self.third_side) / 2 - self.third_side)))

    def calculate_square_wtih_two_side(self):
        square = 1
        corner = 0
        for i in list(name for name in self.__dict__ if name.endswith('_side')):
            if self.__dict__[i] > 0:
                square = square * self.__dict__[i]
        for i in list(name for name in self.__dict__ if name.endswith('_corner')):
            if self.__dict__[i] != 0:
                corner = self.__dict__[i]
        return 0.5 * (float(square)) * math.sin(float(corner))
