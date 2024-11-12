import pytest
import re

def test_empty_string():
    assert find_max_number("") is None

def test_no_numbers():
    assert find_max_number("abcde") is None

def test_single_digit():
    assert find_max_number("a1b2c3") == 3

def test_multiple_numbers():
    assert find_max_number("12ab29cd19") == 29

def test_leading_zeroes():
    assert find_max_number("00001234abc") == 1234

def test_large_numbers():
    assert find_max_number("number9999999999999999") == 9999999999999999

def test_max_length_string():
    input_string = "a" * 100000 + "12345"  # 100,000 characters long
    assert find_max_number(input_string) == 12345

def test_high_boundary_number():
    assert find_max_number("extra9876543212345") == 9876543212345

def test_numbers_in_various_cases():
    assert find_max_number("abc1de2f3g4h5i6j7k8l9m0") == 9

def test_find_largest_number_from_string_with_single_digit():
    assert find_largest_number_from_string("3a") == 3

def test_find_largest_number_from_string_with_no_digits():
    assert find_largest_number_from_string("abc") == -1

