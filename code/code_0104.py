def find_min_number(s):
    s += "*"
    res = 10 ** 19
    x = 0
    l = len(s)
    for i in range(0, l - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = min(res, x)
                x = 0
    return res