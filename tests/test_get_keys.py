import pytest
from gendiff.modules.get_keys import get_keys
from tests.fixtures.data_test import test_variants_for_get_keys


@pytest.mark.parametrize("dict1,dict2,expected", test_variants_for_get_keys)
def test_get_keys(dict1, dict2, expected):
    assert get_keys(dict1, dict2) == expected
