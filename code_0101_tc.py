import pytest
from code_0101 import remaining_elements_count

def test_empty_list():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([5]) == 1

def test_two_odd_elements():
    assert remaining_elements_count([3, 7]) == 2

def test_two_even_elements():
    assert remaining_elements_count([2, 4]) == 2

def test_odd_even_removal():
    assert remaining_elements_count([1, 2]) == 1

def test_even_odd_removal():
    assert remaining_elements_count([4, 1]) == 1

def test_multiple_elements_no_removal():
    assert remaining_elements_count([1, 3, 5]) == 3

def test_multiple_elements_with_removal():
    assert remaining_elements_count([1, 2, 3, 4]) == 1

def test_large_alternating_elements():
    assert remaining_elements_count([1, 2] * 50) == 1

def test_large_all_same_elements():
    assert remaining_elements_count([2] * 100) == 100