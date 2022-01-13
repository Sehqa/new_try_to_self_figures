import pickle
import const
from .tools_for_file import ToolsForFile

class CheckTools:
    @staticmethod
    def check_figure_from_file(object, parameter_for_figures='guid'):
        """
        Проверка того что обьект есть в файле.
        :param object;
        :param parameter_for_figures;
        :return;
        """
        for item in ToolsForFile.get_data_from_file():
            if item.__dict__ == object.__dict__:
                return True
        return False

    @staticmethod
    def check_figure_with_square(criteria):
        """
        Проверяем что фигуры удалены согласно критерию.
        :param criteria:
        :return:
        """
        for item in list(pickle.load(open(const.DATA_FILE_NAME, 'rb'))):
            if float(item.square) < float(criteria):
                return False
        return True
