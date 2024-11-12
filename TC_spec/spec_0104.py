import pytest
from function.function_0104 import find_min_number

def test_find_min_number_with_single_digit():
    assert find_min_number("5") == 5

def test_find_min_number_with_multiple_digits():
    assert find_min_number("abc1234") == 1234

def test_find_min_number_with_multiple_numbers():
    assert find_min_number("12ab29cd19") == 12

def test_find_min_number_with_no_digits():
    assert find_min_number("abc") == None

def test_find_min_number_with_leading_zeroes():
    assert find_min_number("0042abc24") == 24

def test_find_min_number_with_large_numbers():
    assert find_min_number("999999999912345678") == 12345678

def test_find_min_number_with_edge_case_empty_string():
    assert find_min_number("") == None

def test_find_min_number_with_max_length():
    assert find_min_number("a" * 99999 + "1") == 1