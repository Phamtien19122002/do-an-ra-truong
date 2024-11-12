import pytest
from function.function_0104 import find_min_number

def test_find_min_number_single_digit():
    assert find_min_number("7a") == 7

def test_find_min_number_multiple_digits():
    assert find_min_number("45b") == 45

def test_find_min_number_leading_zero():
    assert find_min_number("004c") == 4

def test_find_min_number_with_letters():
    assert find_min_number("abc5d") == 5

def test_find_min_number_empty_string():
    assert find_min_number("") == 10**19

def test_find_min_number_no_digits():
    assert find_min_number("abcdefg") == 10**19

def test_find_min_number_mixed_content():
    assert find_min_number("12ab34cd2ef") == 2

def test_find_min_number_boundary_large_number():
    assert find_min_number("9999999999d") == 9999999999

def test_find_min_number_no_alphabet_after_digits():
    assert find_min_number("123") == 10**19

def test_find_min_number_just_above_zero():
    assert find_min_number("0a") == 0