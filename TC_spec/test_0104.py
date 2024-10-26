import pytest, re

def find_smallest_number(s):
    numbers = re.findall(r'\d+', s)
    return min(int(num) for num in numbers) if numbers else None

def test_find_smallest_in_single_number():
    assert find_smallest_number("1abc") == 1

def test_find_smallest_in_multiple_numbers():
    assert find_smallest_number("12ab29cd19") == 12

def test_find_smallest_in_numbers_with_leading_zeroes():
    assert find_smallest_number("ab003cd00") == 0

def test_find_smallest_with_no_numbers():
    assert find_smallest_number("abcdef") is None

def test_find_smallest_in_large_numbers():
    assert find_smallest_number("12ab34567890123456789cd19") == 12

def test_find_smallest_in_numbers_with_mixed_characters():
    assert find_smallest_number("xyz9w8v7u6t5y4z3c2b1a0") == 0

def test_find_smallest_with_boundary_length():
    assert find_smallest_number("a" * 99999 + "1") == 1

def test_find_smallest_with_edge_case_empty_string():
    assert find_smallest_number("") is None