import pytest
from function import calculate_income_tax

def test_calculate_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

def test_calculate_income_tax_boundary_just_above_zero():
    assert calculate_income_tax(1) == 0.05

def test_calculate_income_tax_boundary_at_5000():
    assert calculate_income_tax(5000) == 250

def test_calculate_income_tax_boundary_just_above_5000():
    assert calculate_income_tax(5001) == 250.05

def test_calculate_income_tax_boundary_at_10000():
    assert calculate_income_tax(10000) == 750

def test_calculate_income_tax_boundary_just_above_10000():
    assert calculate_income_tax(10001) == 750.15

def test_calculate_income_tax_boundary_at_20000():
    assert calculate_income_tax(20000) == 2250

def test_calculate_income_tax_boundary_just_above_20000():
    assert calculate_income_tax(20001) == 2250.15

def test_calculate_income_tax_boundary_at_50000():
    assert calculate_income_tax(50000) == 9250

def test_calculate_income_tax_boundary_just_above_50000():
    assert calculate_income_tax(50001) == 9250.25

def test_calculate_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

def test_calculate_income_tax_small_income():
    assert calculate_income_tax(5000) == 250

def test_calculate_income_tax_mid_income():
    assert calculate_income_tax(10000) == 750

def test_calculate_income_tax_high_income():
    assert calculate_income_tax(20000) == 2250

def test_calculate_income_tax_upper_income():
    assert calculate_income_tax(50000) == 10000

def test_calculate_income_tax_very_high_income():
    assert calculate_income_tax(100000) == 20000

def test_calculate_income_tax_zero_income():
    assert calculate_income_tax(0) == 0

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