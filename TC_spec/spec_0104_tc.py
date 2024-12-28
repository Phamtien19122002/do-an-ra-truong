import pytest
from code_0104 import find_min_number

def test_single_digit():
    assert find_min_number("9") == 9

def test_two_digit_number():
    assert find_min_number("47") == 47

def test_leading_zero_ignored():
    assert find_min_number("0034") == 34

def test_multiple_numbers_with_letters():
    assert find_min_number("abc123def456") == 123

def test_only_letters():
    assert find_min_number("abcdefg") is None

def test_only_numbers():
    assert find_min_number("9876543210") == 0

def test_boundary_case_max_length():
    assert find_min_number("1" * 100000) == 1

def test_single_large_number():  #update
    assert find_min_number("123456789012345678") == 123456789012345678

def test_numbers_with_special_chars():
    assert find_min_number("abc$%^123") == 123

def test_empty_string():
    assert find_min_number("") is None
