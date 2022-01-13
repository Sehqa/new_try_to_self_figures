import pytest
import const

from  tools.tools_for_delete import ToolsForDelete
from tools.tools_for_file import ToolsForFile


@pytest.fixture(scope="function", params=const.LIST_WITH_TEST_FIGURES)
def fixture_generate_figures(request):
    return request.param


@pytest.fixture(scope='function')
def fixture_delete_figures():
    yield
    for item in const.LIST_WITH_TEST_FIGURES:
        ToolsForDelete.delete_create_figure(item)


@pytest.fixture(scope="function")
def fixture_write_to_file():
    ToolsForFile.write_to_file([], filename='myfile.pkl')


def fixture_generate_get_data(request):
    ToolsForFile.write_to_file(const.LIST_WITH_TEST_FIGURES, filename='myfile.pkl')
    return request.param
