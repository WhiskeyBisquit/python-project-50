import json


def parse(file_path):
    file_dict = json.load(open(file_path))
    for el in file_dict:
        if file_dict[el] is True:
            file_dict[el] = 'true'
        elif file_dict[el] is False:
            file_dict[el] = 'false'
    return file_dict
