import pytest
from gendiff.modules.parse import parse
from tests.fixtures.data_test import test_variants_for_parsing


@pytest.mark.parametrize("path1,path2,expected", test_variants_for_parsing)
def test_parse(path1, path2, expected):
    assert parse(path1, path2) == expected
