from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish
from gendiff.modules.get_keys import get_keys
from gendiff.modules.parse import parse


def get_diff(d1: dict, d2: dict):
    result = {}
    all_keys = get_keys(d1, d2)

    for key in all_keys:
        negativ_key = f'- {key}'
        positive_key = f'+ {key}'

        if key in d1 and key in d2:
            if d1[key] == d2[key]:
                result[f'  {key}'] = d1[key]
            elif d1[key] != d2[key] and not isinstance(d2[key], dict):
                result[negativ_key] = d1[key]
                result[positive_key] = d2[key]
        if key not in d2:
            result[negativ_key] = d1[key]
        if key in d2 and key not in d1:
            result[positive_key] = d2[key]

    return result


def get_nested_diff(d1: dict, d2: dict):
    result = {}
    all_keys = get_keys(d1, d2)

    for key in all_keys:
        if not isinstance(d2.get(key, ''), dict):
            result.update(get_diff(d1, d2))
        elif key in d1 and key in d2:
            result[key] = get_nested_diff(d1[key], d2[key])

    return result


def generate_diff(file_path1: str, file_path2: str, formatter='stylish'):
    dict1 = parse(file_path1)
    dict2 = parse(file_path2)

    if formatter == 'plain':
        return get_plain(dict1, dict2)
    elif formatter not in ['plain', 'stylish']:
        return f"""gendiff doesn\'t support '{formatter}' formatter. 
Please try 'stylish' or 'plain'"""
    else:
        diff = get_nested_diff(dict1, dict2)
        return get_stylish(diff)
