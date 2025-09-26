def get_stylish(diff):
    result = "{\n"
    level = 1

    def walk(diff):
        nonlocal level
        nonlocal result
        spaces = '    '
        enter = "{\n"
        exit_ = "}\n"
        tabs = level * spaces

        for k, v in diff.items():
            if isinstance(v, dict):
                if k[0] not in [' ', '-', '+']:
                    result += f"{tabs}{k}: {enter}"
                    level += 1
                    walk(v)
                else:
                    result += f"{tabs[:-2]}{k}: {enter}"
                    level += 1
                    walk(v)
            elif k[0] in [' ', '-', '+']:
                result += f"{tabs[:-2]}{k}: {v}\n"
            else:
                result += f"{tabs}{k}: {v}\n"
        result += f"{tabs[:-4]}{exit_}"
        level -= 1

    walk(diff)

    return result.strip()
