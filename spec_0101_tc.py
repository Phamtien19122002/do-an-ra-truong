import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([1]) == 1

def test_remaining_elements_count_two_odd_elements():
    assert remaining_elements_count([1, 3]) == 2

def test_remaining_elements_count_two_even_elements():
    assert remaining_elements_count([2, 4]) == 0

def test_remaining_elements_count_mixed_even_odd():
    assert remaining_elements_count([1, 2]) == 1

def test_remaining_elements_count_multiple_pairs_removal():
    assert remaining_elements_count([2, 4, 6, 1, 3]) == 3

def test_remaining_elements_count_all_odd_elements():
    assert remaining_elements_count([3, 5, 7, 9]) == 4

def test_remaining_elements_count_all_even_elements():
    assert remaining_elements_count([2, 2, 2, 2]) == 0

def test_remaining_elements_count_large_mixed_case():
    assert remaining_elements_count([5, 1, 6, 2, 3, 4, 8, 10]) == 3