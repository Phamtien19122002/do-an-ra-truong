import pytest

def find_min_number(s):
    s += "*"
    res = 10 ** 19
    x = 0
    l = len(s)
    for i in range(0, l - 1):
        if s[i].isdigit():
            x = x * 10 + int(s[i])
            if s[i + 1].isalpha():
                res = min(res, x)
                x = 0
    return res

def test_find_min_number_single_digit():
    assert find_min_number("5a") == 5

def test_find_min_number_multiple_digits():
    assert find_min_number("23b") == 23

def test_find_min_number_leading_zero_ignored():
    assert find_min_number("012c") == 12

def test_find_min_number_two_numbers():
    assert find_min_number("34d56e") == 34

def test_find_min_number_no_digits():
    assert find_min_number("abc") == 10**19

def test_find_min_number_only_spaces():
    assert find_min_number("   a") == 10**19

def test_find_min_number_number_followed_by_special_char():
    assert find_min_number("78@") == 78

def test_find_min_number_multiple_numbers():
    assert find_min_number("5a7b3c") == 3

def test_find_min_number_large_number():
    assert find_min_number("1000d") == 1000

def test_find_min_number_empty_string():
    assert find_min_number("") == 10**19