import pytest
from function import calculate_income_tax
def test_income_tax_negative_income():
    assert calculate_income_tax(-100) == 0

def test_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

def test_income_tax_low_income():
    assert calculate_income_tax(4000) == 200

def test_income_tax_middle_income1():
    assert calculate_income_tax(6000) == 550

def test_income_tax_middle_income2():
    assert calculate_income_tax(15000) == 1750

def test_income_tax_high_income1():
    assert calculate_income_tax(25000) == 3750

def test_income_tax_high_income2():
    assert calculate_income_tax(60000) == 10750

def test_calculate_income_tax_low_income():
    assert calculate_income_tax(3000) == 3000 * 0.05

def test_calculate_income_tax_high_income_below_10000():
    assert calculate_income_tax(7000) == 5000 * 0.05 + (7000 - 5000) * 0.1

def test_calculate_income_tax_high_income_below_20000():
    assert calculate_income_tax(15000) == 5000 * 0.05 + 5000 * 0.1 + (15000 - 10000) * 0.15

def test_calculate_income_tax_high_income_below_50000():
    assert calculate_income_tax(30000) == 5000 * 0.05 + 5000 * 0.1 + 10000 * 0.15 + (30000 - 20000) * 0.2

def test_calculate_income_tax_high_income_above_50000():
    assert calculate_income_tax(60000) == 5000 * 0.05 + 5000 * 0.1 + 10000 * 0.15 + 30000 * 0.2 + (60000 - 50000) * 0.25

