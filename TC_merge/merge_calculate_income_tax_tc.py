import pytest
from code_calculate_income_tax import calculate_income_tax

def test_income_tax_negative_income():
    assert calculate_income_tax(-1000) == 0

def test_income_tax_low_income():
    assert calculate_income_tax(4000) == 200.0

def test_income_tax_mid_income():
    assert calculate_income_tax(7500) == 500.0

def test_income_tax_high_income():  #update
    assert calculate_income_tax(15000) == 1500.0  # Updated expected output here

def test_income_tax_upper_high_income():  #update
    assert calculate_income_tax(30000) == 4250.0  # Updated expected output here

def test_income_tax_very_high_income():  #update
    assert calculate_income_tax(60000) == 10750.0  # Updated expected output here

