import pytest
from code_0104 import find_min_number

def test_find_min_number_single_digit():
    assert find_min_number("a2b3c") == 2

def test_find_min_number_multiple_digits():
    assert find_min_number("ab12cd34ef") == 12

def test_find_min_number_leading_zeros():
    assert find_min_number("abc01de23") == 1

def test_find_min_number_boundary_case_min_length():
    assert find_min_number("a1") == 1  # unchanged

def test_find_min_number_boundary_case_max_length():
    assert find_min_number("a" * 99999 + "9") == 9  # unchanged

def test_find_min_number_large_number():  #update
    assert find_min_number("abc999999999999999") == '999999999999999999'  #update

# Additional tests could be added below this line
