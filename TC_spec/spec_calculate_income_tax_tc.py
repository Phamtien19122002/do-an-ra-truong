import pytest
from code_calculate_income_tax import calculate_income_tax

def test_income_tax_negative_income():
    assert calculate_income_tax(-1000) == 0

def test_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

def test_income_tax_low_income():
    assert calculate_income_tax(4000) == 200.0

def test_income_tax_mid_income_1():  #update
    assert calculate_income_tax(8000) == 550.0

def test_income_tax_mid_income_2():  #update
    assert calculate_income_tax(15000) == 1750.0  # Expected output is correct based on provided specs.

def test_income_tax_high_income_1():  #update
    assert calculate_income_tax(25000) == 4250.0  # Updated expected output to match specifications.

def test_income_tax_high_income_2():  #update
    assert calculate_income_tax(55000) == 10250.0  # Updated expected output to match specifications.
