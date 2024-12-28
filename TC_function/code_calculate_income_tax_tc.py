import pytest
from code_calculate_income_tax import calculate_income_tax

def test_calculate_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

def test_calculate_income_tax_small_income():
    assert calculate_income_tax(3000) == 150

def test_calculate_income_tax_boundary_income_5000():
    assert calculate_income_tax(5000) == 250

def test_calculate_income_tax_mid_income():
    assert calculate_income_tax(7500) == 500

def test_calculate_income_tax_boundary_income_10000():
    assert calculate_income_tax(10000) == 750

def test_calculate_income_tax_high_income():  #update
    assert calculate_income_tax(15000) == 1500

def test_calculate_income_tax_boundary_income_20000():  #update
    assert calculate_income_tax(20000) == 3250

def test_calculate_income_tax_above_average_income():  #update
    assert calculate_income_tax(30000) == 6250

def test_calculate_income_tax_boundary_income_50000():  #update
    assert calculate_income_tax(50000) == 10000

def test_calculate_income_tax_highest_income():  #update
    assert calculate_income_tax(75000) == 18750
