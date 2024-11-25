import pytest
from function.function_0105 import find_largest_number_from_string

def test_find_largest_number_with_single_digits():
    assert find_largest_number_from_string("3 2 1") == 3

def test_find_largest_number_with_multiple_digits():
    assert find_largest_number_from_string("42 100 7") == 100

def test_find_largest_number_with_leading_zeros():
    assert find_largest_number_from_string("007 8 9") == 9

def test_find_largest_number_with_no_digits():
    assert find_largest_number_from_string("abc def") == -1

def test_find_largest_number_with_alphanumeric():
    assert find_largest_number_from_string("3x 4y 5z") == 5

def test_find_largest_number_with_empty_string():
    assert find_largest_number_from_string("") == -1

def test_find_largest_number_with_special_characters():
    assert find_largest_number_from_string("!@#5$%^") == 5

def test_find_largest_number_with_consecutive_digits():
    assert find_largest_number_from_string("12345abc") == 12345

def test_find_largest_number_with_mixed_characters():
    assert find_largest_number_from_string("1a2b3c") == 3

def test_find_largest_number_with_single_large_number():
    assert find_largest_number_from_string("9999") == 9999