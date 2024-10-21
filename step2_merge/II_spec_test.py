import pytest
from II_code import find_min_number

def test_find_min_number_with_mixed_characters():
    input_str = "12ab29cd19"
    expected = 12
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_sequential_numbers():
    input_str = "ab123gh456cd"
    expected = 123
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_single_digits():
    input_str = "a1b2c3d4"
    expected = 1
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_leading_zeros():
    input_str = "000999111"
    expected = 999111
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_no_numbers():
    input_str = "abcxyz"
    expected = None
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_large_numbers():
    input_str = "1001ab1234cd5678"
    expected = 1001
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_only_zero():
    assert find_min_number("000") == 0

def test_find_min_number_with_empty_string():
    input_str = ""
    expected = 10 ** 19
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_number_with_no_digits():
    input_str = "noNumbersHere"
    expected = 10 ** 19
    result = find_min_number(input_str)
    assert result == expected, f"Expected {expected}, got {result}"
