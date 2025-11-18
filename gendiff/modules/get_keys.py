def get_keys(d1: dict, d2: dict):
    if isinstance(d1, dict) and isinstance(d2, dict):
        return sorted(d1.keys() | d2.keys())
    else:
        raise TypeError("non-iterable object")
