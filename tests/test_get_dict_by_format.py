import pytest
from gendiff.modules.get_dict_by_format import get_dict_by_format
from tests.fixtures.data_test import test_variants__for_gdbf


@pytest.mark.parametrize("path,expected", test_variants__for_gdbf)
def test_get_dict_by_format(path, expected):
    assert get_dict_by_format(path) == expected
