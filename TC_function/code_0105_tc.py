import pytest
from code_0105 import find_largest_number_from_string

def test_find_largest_number_with_single_digit():
    assert find_largest_number_from_string("5") == 5

def test_find_largest_number_with_multiple_digits():
    assert find_largest_number_from_string("123abc456") == 456

def test_find_largest_number_with_only_digits():
    assert find_largest_number_from_string("7890") == 7890

def test_find_largest_number_with_no_digits():  #update
    assert find_largest_number_from_string("abc") == 0  #update

def test_find_largest_number_with_leading_zeros():
    assert find_largest_number_from_string("07and23") == 23

def test_find_largest_number_with_special_characters():  #update
    assert find_largest_number_from_string("@#13.45abc78?") == 78  # The correct output here is 78

def test_find_largest_number_with_negative_numbers():  #update
    assert find_largest_number_from_string("-5abc-10def-20") == 20  #update, the largest number is 20

def test_find_largest_number_with_empty_string():  #update
    assert find_largest_number_from_string("") == 0  #update

def test_find_largest_number_with_single_alphabet():  #update
    assert find_largest_number_from_string("a") == 0  #update

def test_find_largest_number_boundary_cases():
    assert find_largest_number_from_string("0abc") == 0
