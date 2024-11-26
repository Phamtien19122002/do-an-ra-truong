import pytest
from function.function_0101 import remaining_elements_count

def test_remaining_elements_count_with_even_numbers():
    assert remaining_elements_count([2, 4, 6, 8]) == 4

def test_remaining_elements_count_with_odd_numbers():
    assert remaining_elements_count([1, 3, 5, 7]) == 4

def test_remaining_elements_count_with_mixed_numbers_even_odd():
    assert remaining_elements_count([1, 2, 3, 4, 5]) == 3

def test_remaining_elements_count_with_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_with_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_with_identical_elements():
    assert remaining_elements_count([1, 1, 1, 1]) == 1

def test_remaining_elements_count_with_negative_numbers():
    assert remaining_elements_count([-1, -2, -3, -4]) == 4

def test_remaining_elements_count_with_boundary_case():
    assert remaining_elements_count([2, 3]) == 2

def test_remaining_elements_count_with_large_numbers():
    assert remaining_elements_count([1000000, 2000000, 3000000, 4000000]) == 4

def test_remaining_elements_count_with_alternating_even_odd():
    assert remaining_elements_count([1, 2, 1, 2]) == 2