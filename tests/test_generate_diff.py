from gendiff.generate_diff import generate_diff


file_path1 = 'tests/fixtures/file1.json'
file_path2 = 'tests/fixtures/file2.json'

expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff():
    assert generate_diff(file_path1, file_path2) == expected
