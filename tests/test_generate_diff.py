import pytest

from gendiff.generate_diff import generate_diff
from tests.test_data.test_data import test_variants


@pytest.mark.parametrize("dict1,dict2,expected", test_variants)
def test_generate_diff(dict1, dict2, expected):
    assert generate_diff(dict1, dict2) == expected
