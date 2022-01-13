import pytest
from tools.tools import Tools
from figures.square import Square
from  tools.tools_for_delete import ToolsForDelete
from tools.tools_for_file import ToolsForFile
from tools.check_tools import CheckTools

# Тест на добавление (проверяем есть ли данные в файле после метода add_new_figure) а после удаляем данные.

def test_add_figure(fixture_generate_figures, fixture_delete_figures):
    Tools.add_new_figure(object_figure=fixture_generate_figures)
    assert CheckTools.check_figure_from_file(fixture_generate_figures) == True



# Тест на удаление по критерию площади, проверяем что нет фигур

@pytest.mark.parametrize('criteria', [300, '3fsdf'])
def test_delete_figure_with_square_criteria(criteria):
    ToolsForDelete.delete_figures_with_square_criteria(criteria)
    assert CheckTools.check_figure_with_square(criteria) == True


# Проверяем запись в файл
@pytest.mark.parametrize('obj', [Square('Square1', 55), '3fsdf'])
def test_write_to_file(obj):
    ToolsForFile.write_to_file([obj])
    assert CheckTools.check_figure_from_file(obj)
