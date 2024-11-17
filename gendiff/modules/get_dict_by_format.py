import json
import yaml


def get_dict_by_format(file_path):
    format_ = file_path.split('.')[-1].lower()
    file_dict = {}
    if format_ == 'json':
        file_dict = json.load(open(file_path))
    else:
        with (open(file_path, 'r')) as file:
            file_dict = yaml.load(file, Loader=yaml.SafeLoader)
    return file_dict
