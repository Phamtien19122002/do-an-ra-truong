import pytest
from code_0101 import remaining_elements_count
def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_odd_elements():
    assert remaining_elements_count([3, 5]) == 2

def test_remaining_elements_count_two_even_elements():
    assert remaining_elements_count([2, 4]) == 0

def test_remaining_elements_count_even_and_odd():
    assert remaining_elements_count([1, 2, 3, 4]) == 2

def test_remaining_elements_count_alternating_odds_and_evens():
    assert remaining_elements_count([1, 2, 1, 2]) == 4

def test_remaining_elements_count_large_sequence():
    assert remaining_elements_count([1] * 100000) == 100000

def test_remaining_elements_count_two_pairs_remain():
    assert remaining_elements_count([1, 2, 1, 2, 5, 4]) == 4

def test_remaining_elements_count_all_even_and_odd():
    assert remaining_elements_count([2, 3, 4, 5]) == 4

def test_remaining_elements_count_empty():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_one_odd_one_even():
    assert remaining_elements_count([1, 2]) == 1

def test_remaining_elements_count_three_elements_all_odd():
    assert remaining_elements_count([1, 3, 5]) == 3

