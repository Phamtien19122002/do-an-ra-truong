def remaining_elements_count(a):
    res = []
    for i in a:
        if len(res) == 0:
            res.append(i)
        else:
            if (res[-1] + i) % 2 == 0:
                res.pop()
            else:
                res.append(i)
    return len(res)