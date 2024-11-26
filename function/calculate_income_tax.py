def calculate_income_tax(income):
    if income <= 0:
        return 0
    elif income <= 5000:
        return income * 0.05
    elif income <= 10000:
        return 5000 * 0.05 + (income - 5000) * 0.1
    elif income <= 20000:
        return 5000 * 0.05 + 5000 * 0.1 + (income - 10000) * 0.15
    elif income <= 50000:
        return 5000 * 0.05 + 5000 * 0.1 + 10000 * 0.15 + (income - 20000) * 0.2
    else:
        return 5000 * 0.05 + 5000 * 0.1 + 10000 * 0.15 + 30000 * 0.2 + (income - 50000) * 0.25