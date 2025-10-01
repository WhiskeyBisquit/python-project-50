import pytest

from gendiff.scripts.gendiff import main

#  data for test gendiff -h --help
gendiff_help = """[-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output"""


def test_main(capsys):
    with pytest.raises(SystemExit):
        main(["--help"])
    captured = capsys.readouterr()
    assert gendiff_help in captured.out