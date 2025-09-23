from modules.get_keys import get_keys


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


def generate_diff(d1: dict, d2: dict):
    result = {}
    all_keys = get_keys(d1, d2)

    for key in all_keys:
        if not isinstance(d2.get(key, ''), dict):
            result.update(get_diff(d1, d2))
        elif key in d1 and key in d2:
            result[key] = generate_diff(d1[key], d2[key])

    return result
