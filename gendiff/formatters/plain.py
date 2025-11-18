from gendiff.modules.get_keys import get_keys


# def check_the_value(value):
#     if value in ['false', 'true', 'null']:
#         return value
#     elif isinstance(value, int):
#         return value
#     else:
#         return f"'{value}'"
def check_the_value(value):
    if value in ['false', 'true', 'null']:
        return value
    elif isinstance(value, int):
        return value
    elif isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    else:
        return f"'{value}'"


def get_plain(d1: dict, d2: dict):  # noqa: C901
    result = ''
    cur_key = []

    def walk(d1, d2):  # noqa: C901
        nonlocal result
        nonlocal cur_key

        if isinstance(d1, dict) and isinstance(d2, dict):
            all_keys = get_keys(d1, d2)
        else:
            return

        for key in all_keys:
            cur_key.append(key)
            new_key = ".".join(cur_key)

            if key in d1 and key in d2:
                if d1[key] == d2[key]:
                    del cur_key[-1]
                    continue

                if d1[key] != d2[key] and not isinstance(d2[key], dict):
                    if isinstance(d1[key], dict):
                        result += f"Property '{new_key}' was updated. From [complex value] to {check_the_value(d2[key])}\n"  # noqa: E501
                    elif isinstance(d2[key], dict):
                        result += f"Property '{new_key}' was updated. From {check_the_value(d1[key])} to [complex value]\n"  # noqa: E501
                    else:
                        result += f"Property '{new_key}' was updated. From {check_the_value(d1[key])} to {check_the_value(d2[key])}\n"  # noqa: E501
                else:
                    walk(d1[key], d2[key])

            if key not in d2:
                result += f"Property '{new_key}' was removed\n"

            if key in d2 and key not in d1:
                if isinstance(d2[key], dict):
                    result += f"Property '{new_key}' was added with value: [complex value]\n"  # noqa: E501
                else:
                    result += f"Property '{new_key}' was added with value: {check_the_value(d2[key])}\n"  # noqa: E501

            if cur_key:
                del cur_key[-1]

    walk(d1, d2)
    return result.strip()


# def get_plain(d1: dict, d2: dict):  # noqa: C901
#     result = ''
#     cur_key = []

#     def walk(d1, d2):  # noqa: C901
#         nonlocal result
#         nonlocal cur_key
#         if isinstance(d1, dict) and isinstance(d2, dict):
#             all_keys = get_keys(d1, d2)
#         else:
#             return

#         for key in all_keys:
#             cur_key.append(key)
#             new_key = ".".join(cur_key)

#             if key in d1 and key in d2:
#                 if d1[key] == d2[key]:
#                     del cur_key[-1]
#                     continue
#                 if d1[key] != d2[key] and not isinstance(d2[key], dict):
#                     if isinstance(d1[key], dict):
#                         result += f"Property '{new_key}' was updated. From [complex value] to {check_the_value(d2[key])}\n"  # noqa: E501
#                     elif isinstance(d2[key], dict):
#                         result += f"Property '{new_key}' was updated. From {check_the_value(d1[key])} to [complex value]\n"  # noqa: E501
#                     else:
#                         result += f"Property '{new_key}' was updated. From {check_the_value(d1[key])} to {check_the_value(d2[key])}\n"  # noqa: E501
#                 else:
#                     walk(d1[key], d2[key])

#             if key not in d2:
#                 result += f"Property '{new_key}' was removed\n"

#             if key in d2 and key not in d1:
#                 if isinstance(d2[key], dict):
#                     result += f"Property '{new_key}' was added with value: [complex value]\n"  # noqa: E501
#                 else:
#                     result += f"Property '{new_key}' was added with value: {check_the_value(d2[key])}\n"  # noqa: E501

#             if cur_key:
#                 del cur_key[-1]

#     walk(d1, d2)
#     return result.strip()
