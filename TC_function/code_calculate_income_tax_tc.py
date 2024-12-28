import pytest
from code_calculate_income_tax import calculate_income_tax

def test_calculate_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

def test_calculate_income_tax_low_income():
    assert calculate_income_tax(4000) == 200

def test_calculate_income_tax_exact_boundary_low():
    assert calculate_income_tax(5000) == 250

def test_calculate_income_tax_mid_range_income():
    assert calculate_income_tax(7500) == 500

def test_calculate_income_tax_high_range_income():  #update
    assert calculate_income_tax(15000) == 1500.0  # updated to 1500.0

def test_calculate_income_tax_exact_boundary_high():  #update
    assert calculate_income_tax(20000) == 2250 # updated to 2250.0 (was correct)

def test_calculate_income_tax_above_high_boundary():  #update
    assert calculate_income_tax(30000) == 4250.0  # updated to 4250.0

def test_calculate_income_tax_above_max_limit():  #update
    assert calculate_income_tax(60000) == 10750.0  # updated to 10750.0
