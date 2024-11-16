from gendiff.modules.parse import parse


def generate_diff(file_path1, file_path2):
    file_dict1 = dict(sorted(parse(file_path1).items()))
    file_dict2 = dict(sorted(parse(file_path2).items()))

    result_str = '{\n'
    for key in file_dict1:
        key_value1 = f'{key}: {file_dict1[key]}' if key in file_dict1 else ''
        key_value2 = f'{key}: {file_dict2[key]}' if key in file_dict2 else ''
        if key in file_dict2 and file_dict1[key] == file_dict2[key]:
            result_str += f'    {key_value2}\n'
        elif key in file_dict2 and file_dict1[key] != file_dict2[key]:
            result_str += f'  - {key_value1}\n'
            result_str += f'  + {key_value2}\n'
        else:
            result_str += f'  - {key_value1}\n'

    for el in file_dict2:
        if el not in file_dict1:
            result_str += f'  + {el}: {file_dict2[el]}\n'

    result = result_str + '}'
    return result
