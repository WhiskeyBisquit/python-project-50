from gendiff.formatters.json import get_complex_diff, get_json_diff
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish
from gendiff.modules.get_keys import get_keys
from gendiff.modules.parse import parse


def get_nested_diff(d1, d2):
    result = {}
    all_keys = get_keys(d1, d2)

    for key in all_keys:
        val1 = d1.get(key)
        val2 = d2.get(key)

        if key in d1 and key not in d2:
            result[f"- {key}"] = val1
            continue

        if key in d2 and key not in d1:
            result[f"+ {key}"] = val2
            continue

        if isinstance(val1, dict) and isinstance(val2, dict):
            result[key] = get_nested_diff(val1, val2)
        else:
            if val1 == val2:
                result[f"  {key}"] = val1
            else:
                result[f"- {key}"] = val1
                result[f"+ {key}"] = val2

    return result


def generate_diff(file_path1: str, file_path2: str, formatter='stylish'):
    dict1 = parse(file_path1)
    dict2 = parse(file_path2)

    if formatter == 'plain':
        return get_plain(dict1, dict2)
    elif formatter == 'json':
        diff = get_complex_diff(dict1, dict2)
        return get_json_diff(diff)
    elif formatter not in ['plain', 'stylish', 'json']:
        return f"""gendiff doesn\'t support '{formatter}' formatter. 
Please try 'stylish' / 'plain' / 'json'"""
    else:
        diff = get_nested_diff(dict1, dict2)
        return get_stylish(diff)
