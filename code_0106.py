import math

def convert_to_base(n, s):
    c = ['A', 'B', 'C', 'D', 'E', 'F']
    b = int(math.log(n, 2))
    if n == 2:
        return s
    while len(s) % b != 0:
        s = "0" + s
    result = ""
    i = 0
    while i < len(s):
        tmp = 0
        for j in range(i, i + b):
            tmp += int(s[j]) * (2 ** (b - j + i - 1))
        if tmp < 10:
            result += str(tmp)
        else:
            result += c[tmp - 10]
        i += b
    return result