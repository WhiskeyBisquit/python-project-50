import pytest

from gendiff.generate_diff import generate_diff
from tests.test_data.test_data import test_generate_diff_variants


@pytest.mark.parametrize(
        "file_path1,file_path2,formatter,expected", test_generate_diff_variants)
def test_generate_diff(file_path1, file_path2, formatter, expected):
    assert generate_diff(file_path1, file_path2, formatter) == expected