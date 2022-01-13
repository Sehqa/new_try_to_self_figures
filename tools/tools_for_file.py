import pickle
import const
import os


class ToolsForFile:
    @staticmethod
    def print_all_figures(filename=const.DATA_FILE_NAME):
        """
        Вывод всех фигур.
        :param filename:
        :return:
        """
        if os.path.exists(filename):
            for item in list(pickle.load(open(filename, 'rb'))):
                print(item.__dict__)
            return True
        else:
            return False

    @staticmethod
    def write_to_file(list_with_data, filename=const.DATA_FILE_NAME):
        """
        Вывод в файл списка обьектов.
        :param list_with_data:
        :param filename:
        :return:
        """
        if os.path.exists(filename):
            pickle.dump(list_with_data, open(filename, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
            return True
        else:
            pickle.dump(list_with_data, open(filename, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
            return False

    @staticmethod
    def get_data_from_file(filename=const.DATA_FILE_NAME):
        """
        Получаем список обьектов из файла.
        :param filename:
        :return:
        """
        return list(pickle.load(open(filename, 'rb')))
