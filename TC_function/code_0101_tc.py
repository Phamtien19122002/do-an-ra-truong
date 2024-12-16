import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_with_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_with_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_with_two_even_elements():
    assert remaining_elements_count([2, 4]) == 0  # update

def test_remaining_elements_count_with_two_odd_elements():
    assert remaining_elements_count([3, 5]) == 0  # update

def test_remaining_elements_count_with_one_even_and_one_odd():
    assert remaining_elements_count([2, 3]) == 2

def test_remaining_elements_count_with_consecutive_even_odd():
    assert remaining_elements_count([2, 3, 4]) == 3  # update

def test_remaining_elements_count_with_mixed_numbers():
    assert remaining_elements_count([1, 2, 1, 4, 3]) == 5  # update

def test_remaining_elements_count_with_large_even_list():
    assert remaining_elements_count([2] * 100) == 0  # update

def test_remaining_elements_count_with_large_odd_list():
    assert remaining_elements_count([3] * 100) == 0  # update

def test_remaining_elements_count_with_large_mixed_list():
    assert remaining_elements_count([1, 2] * 50) == 100  # update
