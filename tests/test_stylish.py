import pytest

from gendiff.formatters.stylish import get_stylish
from tests.test_data.test_data import test_stylish_variants


@pytest.mark.parametrize("diff,expected", test_stylish_variants)
def test_get_stylish(diff, expected):
    assert get_stylish(diff) == expected