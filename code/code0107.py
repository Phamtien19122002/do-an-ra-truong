import math

def cv(a, b, p, q):
    a = a.replace(p, q)
    b = b.replace(p, q)
    return int(a) + int(b)

def process_cases(n, cases):
    results = []
    for i in range(n):
        p, q = cases[i][0]
        a, b = cases[i][1]
        x = cv(a, b, p, q)
        y = cv(a, b, q, p)
        results.append((min(x, y), max(x, y)))
    return results