def find_largest_number_from_string(s):
    s += "*"
    res = -1
    x = 0
    l = len(s)
    for i in range(0, l - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = max(res, x)
                x = 0
    return max(res, x)