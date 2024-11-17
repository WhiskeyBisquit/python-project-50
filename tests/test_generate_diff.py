import pytest
from gendiff.generate_diff import generate_diff
from tests.fixtures.data_test import test_variants


@pytest.mark.parametrize("path1,path2,expected", test_variants)
def test_generate_diff(path1, path2, expected):
    assert generate_diff(path1, path2) == expected
