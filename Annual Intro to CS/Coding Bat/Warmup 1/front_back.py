def front_back(str):
    s = list(str)

    if len(s) <= 1:
        return str

    a = str[0]
    b = str[-1]
    between = s[1:-1]
    return b + "".join(between) + a