import pytest
from function.function_0105 import find_largest_number_from_string

def test_large_number_at_start():
    assert find_largest_number_from_string("999abc123") == "999"

def test_large_number_at_end():
    assert find_largest_number_from_string("abc123999") == "999"

def test_large_number_with_special_characters():
    assert find_largest_number_from_string("12ab!29cd19") == "29"

def test_multiple_numbers():
    assert find_largest_number_from_string("12ab29cd99") == "99"

def test_single_digit_numbers():
    assert find_largest_number_from_string("a1b2c3") == "3"

def test_no_numbers():
    assert find_largest_number_from_string("abcdefg") == ""

def test_minimum_length_string():
    assert find_largest_number_from_string("a") == ""

def test_maximum_length_repeated_numbers():
    assert find_largest_number_from_string("1" * 10**5) == "1"

def test_large_numbers_within_boundaries():
    assert find_largest_number_from_string("12ab345678901234567") == "345678901234567"

def test_numbers_with_leading_zeros():
    assert find_largest_number_from_string("00123ab0456") == "456"