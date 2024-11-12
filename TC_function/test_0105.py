import pytest

def find_largest_number_from_string(s):
    s += "*"
    res = -1
    x = 0
    l = len(s)
    for i in range(0, l - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = max(res, x)
                x = 0
    return max(res, x)

def test_find_largest_number_from_string_with_single_digit():
    assert find_largest_number_from_string("3a") == 3

def test_find_largest_number_from_string_with_multiple_digits():
    assert find_largest_number_from_string("42b and 17c") == 42

def test_find_largest_number_from_string_with_no_digits():
    assert find_largest_number_from_string("abc") == -1

def test_find_largest_number_from_string_with_leading_zero():
    assert find_largest_number_from_string("007x") == 7

def test_find_largest_number_from_string_with_empty_string():
    assert find_largest_number_from_string("") == -1

def test_find_largest_number_from_string_with_consecutive_digits():
    assert find_largest_number_from_string("12345x678z") == 678

def test_find_largest_number_from_string_with_non_digit_chars_only():
    assert find_largest_number_from_string("hello") == -1

def test_find_largest_number_from_string_with_negative_numbers():
    assert find_largest_number_from_string("-45a12b") == 12

def test_find_largest_number_from_string_with_long_string():
    assert find_largest_number_from_string("9999999z") == 9999999

def test_find_largest_number_from_string_with_numbers_and_special_chars():
    assert find_largest_number_from_string("23#34$56&78*(90a") == 90