import pytest
from code_0104 import find_min_number

def test_find_min_number_with_single_digit():
    result = find_min_number("3a")
    assert result == 3

def test_find_min_number_with_multiple_digits():
    result = find_min_number("42b")
    assert result == 42

def test_find_min_number_with_no_digits():
    result = find_min_number("abc")
    assert result == 10 ** 19

def test_find_min_number_with_leading_zeros():
    result = find_min_number("003c")
    assert result == 3

def test_find_min_number_with_large_number():
    result = find_min_number("1234567890d")
    assert result == 1234567890

def test_find_min_number_with_four_digit_number():
    result = find_min_number("2022e")
    assert result == 2022

def test_find_min_number_with_multiple_numbers():
    result = find_min_number("5a12b3c")
    assert result == 3

def test_find_min_number_with_empty_string():
    result = find_min_number("")
    assert result == 10 ** 19

def test_find_min_number_with_special_characters():
    result = find_min_number("!@#$%^&*()1a")
    assert result == 1

def test_find_min_number_with_non_digit_character_before_digit():
    result = find_min_number("a1b2c3")
    assert result == 1