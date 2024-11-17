import json


def change_bool(dict_):
    for el in dict_:
        if dict_[el] is True:
            dict_[el] = 'true'
        elif dict_[el] is False:
            dict_[el] = 'false'
    return dict_


def parse(file_path1, file_path2):
    file_dict1 = json.load(open(file_path1))
    file_dict2 = json.load(open(file_path2))

    return change_bool(file_dict1), change_bool(file_dict2)
