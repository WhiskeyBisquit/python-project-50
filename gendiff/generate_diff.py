from gendiff.modules.parse import parse


def generate_diff(file_path1, file_path2):
    file_dict1, file_dict2 = parse(file_path1, file_path2)
    keys = list(set(file_dict1.keys()).union(set(file_dict2.keys())))
    keys.sort()
    result_str = '{\n'
    for key in keys:
        key_value1 = f'{key}: {file_dict1[key]}' if key in file_dict1 else ''
        key_value2 = f'{key}: {file_dict2[key]}' if key in file_dict2 else ''

        if (key in file_dict2
                and key in file_dict1
                and file_dict1[key] == file_dict2[key]):
            result_str += f'    {key_value2}\n'
        elif (key in file_dict2
                and key in file_dict1
                and file_dict1[key] != file_dict2[key]):
            result_str += f'  - {key_value1}\n'
            result_str += f'  + {key_value2}\n'
        elif key in file_dict2 and key not in file_dict1:
            result_str += f'  + {key_value2}\n'
        else:
            result_str += f'  - {key_value1}\n'

    result = result_str + '}'
    return result
