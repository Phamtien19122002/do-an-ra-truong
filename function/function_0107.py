import math

def process_cases(a, b, p, q):
    a_replaced = a.replace(p, q)
    b_replaced = b.replace(p, q)
    x = int(a_replaced) + int(b_replaced)
    
    a_replaced_q = a.replace(q, p)
    b_replaced_q = b.replace(q, p)
    y = int(a_replaced_q) + int(b_replaced_q)
    
    return (min(x, y), max(x, y))

# def process_cases(n, cases):
#     results = []
#     for i in range(n):
#         p, q = cases[i][0]
#         a, b = cases[i][1]
#         x = cv(a, b, p, q)
#         y = cv(a, b, q, p)
#         results.append((min(x, y), max(x, y)))
#     return results

# def cv(a, b, p, q):
#     a = a.replace(p, q)
#     b = b.replace(p, q)
#     return int(a) + int(b)