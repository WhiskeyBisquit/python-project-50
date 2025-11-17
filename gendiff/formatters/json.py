from json import dumps

from gendiff.modules.get_keys import get_keys


def get_plain_diff(d1, d2):
    result = {}
    all_keys = get_keys(d1, d2)
    for key in all_keys:
        if key in d1 and key in d2:
            if d1[key] == d2[key]:
                result[key] = {}
                result[key]['status'] = 'unchanged'
                result[key]['value'] = d2[key]
            elif d1[key] != d2[key] and not isinstance(d2[key], dict):
                result[key] = {}
                result[key]['status'] = 'updated'
                result[key]['value'] = d2[key]
                result[key]['old_value'] = d1[key]
        if key not in d2:
            result[key] = {}
            result[key]['status'] = 'removed'
            result[key]['value'] = d1[key]
        if key in d2 and key not in d1:
            result[key] = {}
            result[key]['status'] = 'added'
            result[key]['value'] = d2[key]

    return result


def get_complex_diff(d1, d2):
    result = {}
    all_keys = get_keys(d1, d2)

    for key in all_keys:
        if not isinstance(d2.get(key, ''), dict):
            result.update(get_plain_diff(d1, d2))
        elif key in d1 and key in d2:
            result[key] = get_complex_diff(d1[key], d2[key])

    return result


def get_json_diff(diff):
    for k, v in diff.items():
        if isinstance(v, dict):
            get_json_diff(v)
        else:
            if diff[k] == 'false':
                diff[k] = False
            elif diff[k] == 'true':
                diff[k] = True
            elif diff[k] == 'null':
                diff[k] = None
    
    return dumps(diff, indent=4)
