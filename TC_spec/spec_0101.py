import pytest
from function.function_0101 import remaining_elements_count

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_even_elements():
    assert remaining_elements_count([2, 4]) == 0

def test_remaining_elements_count_two_odd_elements():
    assert remaining_elements_count([1, 3]) == 2

def test_remaining_elements_count_mixed_even_odd():
    assert remaining_elements_count([1, 2]) == 2

def test_remaining_elements_count_multiple_pairs_removal():
    assert remaining_elements_count([2, 3, 4, 5]) == 2

def test_remaining_elements_count_no_removal():
    assert remaining_elements_count([1, 2, 3]) == 3

def test_remaining_elements_count_alternating_pairs():
    assert remaining_elements_count([1, 2, 1, 2]) == 2

def test_remaining_elements_count_large_input():
    assert remaining_elements_count([1]*100000) == 100000

def test_remaining_elements_count_boundary_even_odd():
    assert remaining_elements_count([100, 1]) == 2

def test_remaining_elements_count_consecutive_removal():
    assert remaining_elements_count([2, 2, 2]) == 0