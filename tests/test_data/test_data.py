from gendiff.generate_diff import generate_diff
from gendiff.modules.parse import parse

#  json
file1_json = 'tests/test_data/file1.json'
file2_json = 'tests/test_data/file2.json'
file3_json = 'tests/test_data/file3.json'
file4_json = 'tests/test_data/file4.json'

j1 = parse(file1_json)
j2 = parse(file2_json)
j3 = parse(file3_json)
j4 = parse(file4_json)

#  yaml
file1_yaml = 'tests/test_data/file1.yaml'
file2_yaml = 'tests/test_data/file2.yaml'
file3_yaml = 'tests/test_data/file3.yaml'
file4_yaml = 'tests/test_data/file4.yaml'

y1 = parse(file1_yaml)
y2 = parse(file2_yaml)
y3 = parse(file3_yaml)
y4 = parse(file4_yaml)


#  data for test generate_diff function
expected = {
    '- follow': 'false',
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': 'true'
}

expected_1 = {
    'common': {
        '+ follow': 'false',
        '  setting1': 'Value 1',
        '- setting2': 200,
        '- setting3': 'true',
        '+ setting3': 'null',
        '+ setting4': 'blah blah',
        '+ setting5': {
            'key5': 'value5'
        },
        'setting6': {
            'doge': {
                '- wow': '',
                '+ wow': 'so much'
            },
            '  key': 'value',
            '+ ops': 'vops'
        }
    },
    'group1': {
        '- baz': 'bas',
        '+ baz': 'bars',
        '  foo': 'bar',
        '- nest': {
            'key': 'value'
        },
        '+ nest': 'str'
    },
    '- group2': {
        'abc': 12345,
        'deep': {
            'id': 45
        }
    },
    '+ group3': {
        'deep': {
            'id': {
                'number': 45
            }
        },
        'fee': 100500
    }
}

test_variants = [
    (j1, j2, expected),
    (y1, y2, expected),
    (j1, y2, expected),
    (y1, j2, expected),
    (j3, j4, expected_1),
    (y3, y4, expected_1),
    (j3, y4, expected_1),
    (y3, j4, expected_1)
]

#  test data for get_stylish function
expected_2 = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

expected_3 = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

test_stylish_variants = [
    (generate_diff(j1, j2), expected_2),
    (generate_diff(y1, y2), expected_2),
    (generate_diff(j1, y2), expected_2),
    (generate_diff(y1, j2), expected_2),
    (generate_diff(j3, j4), expected_3),
    (generate_diff(y3, y4), expected_3),
    (generate_diff(j3, y4), expected_3),
    (generate_diff(y3, j4), expected_3)
]