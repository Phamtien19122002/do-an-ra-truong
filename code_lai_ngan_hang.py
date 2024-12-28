def calculate_years_to_reach_target(N, X, M):
    if N is None or X is None or M is None or (isinstance(N, (int, float)) and N == 0) or (isinstance(X, (int, float)) and X == 0) or (isinstance(M, (int, float)) and M == 0):
        return "None"
    years = 0
    current_amount = N
    while current_amount < M:
        current_amount += current_amount * (X / 100)
        years += 1
    return int(years)