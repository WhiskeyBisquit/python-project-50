from gendiff.modules.parse import parse

file_path1 = 'tests/fixtures/file1.json'
file_path2 = 'tests/fixtures/file2.json'
file_path3 = 'tests/fixtures/file1.yml'
file_path4 = 'tests/fixtures/file2.yml'


# data for test generate_diff function
expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

test_variants = [
    (file_path1, file_path2, expected),
    (file_path3, file_path4, expected),
    (file_path1, file_path4, expected),
    (file_path3, file_path2, expected)
]


# data for test parse function
expected_parsing_result = (
    {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': 'false'
    },
    {'timeout': 20, 'verbose': 'true', 'host': 'hexlet.io'}
)

test_variants_for_parsing = [
    (file_path1, file_path2, expected_parsing_result),
    (file_path3, file_path4, expected_parsing_result),
    (file_path1, file_path4, expected_parsing_result),
    (file_path3, file_path2, expected_parsing_result)
]


# data for test get_keys function
dict1, dict2 = parse(file_path1, file_path4)

expected_get_keys_result = ['follow', 'host', 'proxy', 'timeout', 'verbose']

test_variants_for_get_keys = [
    (dict1, dict2, expected_get_keys_result),
    (dict2, dict1, expected_get_keys_result)
]


# data for test get_dict_by_format function (gdbf)
expected_result1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

expected_result2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}

test_variants__for_gdbf = [
    (file_path1, expected_result1),
    (file_path2, expected_result2),
    (file_path3, expected_result1),
    (file_path4, expected_result2)
]
