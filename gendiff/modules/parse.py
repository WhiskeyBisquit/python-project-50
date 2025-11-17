from json import load

import yaml


def get_dict_by_format(path):
    format_ = path.split('.')[-1].lower()

    if format_ == 'json':
        return load(open(path))
    elif format_ in ['yaml', 'yml']:
        with (open(path, 'r')) as file:
            return yaml.safe_load(file)
    else:
        raise ValueError(f"Unsupported format: {format_}")


def change_bool_null_to_str(dict_):
    for el in dict_:
        if dict_[el] is True:
            dict_[el] = 'true'
        elif dict_[el] is False:
            dict_[el] = 'false'
        elif not dict_[el] and dict_[el] != '':
            dict_[el] = 'null'

        if isinstance(dict_[el], dict):
            change_bool_null_to_str(dict_[el])

    return dict_


def parse(path):
    dict_ = get_dict_by_format(path)
    return change_bool_null_to_str(dict_)
