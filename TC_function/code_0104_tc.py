import pytest
from code_0104 import find_min_number

def test_find_min_number_single_digit():
    assert find_min_number("5a3b2c") == 2

def test_find_min_number_multiple_digits():  #update
    assert find_min_number("45x12y7z") == 7  # The expected output is updated to 7

def test_find_min_number_no_digits():
    assert find_min_number("abcd") == 10**19

def test_find_min_number_only_single_digits():
    assert find_min_number("3a1b4c2d") == 1

def test_find_min_number_leading_zeroes():
    assert find_min_number("005x025y010z") == 5

def test_find_min_number_empty_string():
    assert find_min_number("") == 10**19

def test_find_min_number_consecutive_digits():
    assert find_min_number("123abc456def") == 123

def test_find_min_number_special_characters():
    assert find_min_number("!@#$%^&*()abc55yo") == 55

def test_find_min_number_boundary_digit():
    assert find_min_number("9a8b7c6d5e4f3g2h1i0j") == 0

def test_find_min_number_digits_at_the_end():
    assert find_min_number("hello3world8") == 3
