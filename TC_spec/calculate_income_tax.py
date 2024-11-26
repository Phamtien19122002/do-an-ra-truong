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