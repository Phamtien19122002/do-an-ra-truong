import pytest
from function.function_0101 import remaining_elements_count

def test_remaining_elements_count_single_element_odd():
    assert remaining_elements_count([3]) == 1

def test_remaining_elements_count_single_element_even():
    assert remaining_elements_count([2]) == 1

def test_remaining_elements_count_two_odds():
    assert remaining_elements_count([1, 3]) == 2

def test_remaining_elements_count_two_evens():
    assert remaining_elements_count([2, 4]) == 2

def test_remaining_elements_count_odd_even():
    assert remaining_elements_count([1, 2]) == 1

def test_remaining_elements_count_even_odd():
    assert remaining_elements_count([2, 1]) == 1

def test_remaining_elements_count_multiple_elements_even_length():
    assert remaining_elements_count([1, 2, 3, 4]) == 2

def test_remaining_elements_count_multiple_elements_odd_length():
    assert remaining_elements_count([5, 6, 7]) == 1

def test_remaining_elements_count_boundary_at_zero():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_large_input():
    assert remaining_elements_count([1] * 1000) == 1