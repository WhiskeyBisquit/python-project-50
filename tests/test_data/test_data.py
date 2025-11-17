#  json
file1_json = 'tests/test_data/file1.json'
file2_json = 'tests/test_data/file2.json'
file3_json = 'tests/test_data/file3.json'
file4_json = 'tests/test_data/file4.json'

#  yaml
file1_yaml = 'tests/test_data/file1.yaml'
file2_yaml = 'tests/test_data/file2.yaml'
file3_yaml = 'tests/test_data/file3.yaml'
file4_yaml = 'tests/test_data/file4.yaml'


#  test data for generate_diff function
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

expected_4 = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

expected_5 = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

expected_6 = """gendiff doesn't support 'some_formatter' formatter. 
Please try 'stylish' / 'plain' / 'json'"""

test_generate_diff_variants = [
    (file1_json, file2_json, 'stylish', expected_2),
    (file1_yaml, file2_yaml, 'stylish', expected_2),
    (file1_json, file2_yaml, 'stylish', expected_2),
    (file1_yaml, file2_json, 'stylish', expected_2),
    (file3_json, file4_json, 'stylish', expected_3),
    (file3_yaml, file4_yaml, 'stylish', expected_3),
    (file3_json, file4_yaml, 'stylish', expected_3),
    (file3_yaml, file4_json, 'stylish', expected_3),
    (file1_json, file2_json, 'plain', expected_4),
    (file1_yaml, file2_yaml, 'plain', expected_4),
    (file1_json, file2_yaml, 'plain', expected_4),
    (file1_yaml, file2_json, 'plain', expected_4),
    (file3_json, file4_json, 'plain', expected_5),
    (file3_yaml, file4_yaml, 'plain', expected_5),
    (file3_json, file4_yaml, 'plain', expected_5),
    (file3_yaml, file4_json, 'plain', expected_5),
    (file1_json, file2_json, 'some_formatter', expected_6)
]
