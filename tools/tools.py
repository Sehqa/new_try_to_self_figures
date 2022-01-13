from figures.circle import Circle
from figures.square import Square
from figures.rectangle import Rectangle
from figures.triangle import Triangle
from .tools_for_file import *
from .tools_for_file import  ToolsForFile
from .tools_for_delete import ToolsForDelete
import const
import pickle
import os.path


class Tools:

    @staticmethod
    def add_new_figure(type_figures='type', object_figure=None):
        """
        Добавление новой фигуры.
        :param type_figures:
        :param object_figure:
        :return:
        """
        list_with_data = []
        if os.path.exists(const.DATA_FILE_NAME):
            list_with_data = list(pickle.load(open(const.DATA_FILE_NAME, 'rb')))
        if object_figure is not None:
            list_with_data.append(object_figure)
        elif type_figures == const.LIST_TYPE_FIGURES[0]:
            name_circle = input()
            radius_circle = float(input())
            list_with_data.append(Circle(name_circle, radius_circle))
        elif type_figures == const.LIST_TYPE_FIGURES[1]:
            name = input()
            first_side = float(input())
            second_side = float(input())
            list_with_data.append(Square(name, first_side,second_side))
        elif type_figures == const.LIST_TYPE_FIGURES[2]:
            name = input()
            first_side = float(input())
            second_side = float(input())
            list_with_data.append(Rectangle(name, first_side, second_side))
        elif type_figures == const.LIST_TYPE_FIGURES[3]:
            name = input()
            first_side = float(input())
            second_side = float(input())
            third_side = float(input())
            first_corner = input()
            second_corner = input()
            third_corner = input()
            list_with_data.append(
                Triangle(name, first_side, second_side, third_side, first_corner, second_corner, third_corner))

        ToolsForFile.write_to_file(list_with_data)

    @staticmethod
    def work_menu():
        """
        Метод имитирующий простое меню.
        :return:
        """
        print(
            'Нажмите 1 для вывода списка всех фигур \nНажмите 2 для добавления фигуры \nНажмите 3 для удаления фигур с площадью меньше введенной\nНажмите 4 для выхода')
        menu_item = input()
        if menu_item == '1':
            ToolsForFile.print_all_figures()
        elif menu_item == '2':
            print('Выберите тип фигуры')
            print(f'1: {const.LIST_TYPE_FIGURES[0]} \n2: {const.LIST_TYPE_FIGURES[1]} \n3: {const.LIST_TYPE_FIGURES[2]} \n4: {const.LIST_TYPE_FIGURES[3]}')
            type_figure = input()
            Tools.add_new_figure(type_figure)
        elif menu_item == '3':
            print('Введите площадь и фигуры чья площать меньше указанной будут удалены')
            сriteria = float(input())
            ToolsForDelete.delete_figures_with_square_criteria(сriteria)
        elif menu_item == '4':
            exit(0)
        Tools.work_menu()
