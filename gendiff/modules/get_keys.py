def get_keys(dict1, dict2):
    keys = list(dict1.keys()) + list(
        filter(lambda x: x not in dict1.keys(), dict2.keys()))

    for i in range(1, len(keys)):
        a = keys[i]
        j = i - 1
        while j >= 0 and a < keys[j]:
            keys[j + 1] = keys[j]
            j -= 1
        keys[j + 1] = a

    return keys
