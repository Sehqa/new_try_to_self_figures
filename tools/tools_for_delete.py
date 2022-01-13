import pickle
import const
from  .tools_for_file import ToolsForFile

class ToolsForDelete:
    @staticmethod
    def delete_figures_with_square_criteria(criteria=0):
        """
        Удаление фигур по критерию площади.
        :param criteria:
        :return:
        """
        if criteria == 0:
            criteria = input()
        list_with_data = list(pickle.load(open(const.DATA_FILE_NAME, 'rb')))
        for item in list_with_data:
            if float(item.square) < float(criteria):
                list_with_data.remove(item)
        ToolsForFile.write_to_file(list_with_data)

    @staticmethod
    def delete_create_figure(object):
        """
        Удаление созданных фигур.
        :param object:
        :return:
        """
        list_with_data = list(pickle.load(open(const.DATA_FILE_NAME, 'rb')))
        for item in list_with_data:
            if str(item.guid) == str(object.guid):
                list_with_data.remove(item)
        ToolsForFile.write_to_file(list_with_data)