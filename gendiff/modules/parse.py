from gendiff.modules.get_dict_by_format import get_dict_by_format


def change_bool_to_str(dict_):
    for el in dict_:
        if dict_[el] is True:
            dict_[el] = 'true'
        elif dict_[el] is False:
            dict_[el] = 'false'
    return dict_


def parse(file_path1, file_path2):
    file_dict1 = get_dict_by_format(file_path1)
    file_dict2 = get_dict_by_format(file_path2)

    return change_bool_to_str(file_dict1), change_bool_to_str(file_dict2)
