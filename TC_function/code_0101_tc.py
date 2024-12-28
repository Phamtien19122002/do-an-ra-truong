import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_odd_elements():  # update
    assert remaining_elements_count([1, 3]) == 0  # update

def test_remaining_elements_count_two_even_elements():  # update
    assert remaining_elements_count([2, 4]) == 0  # update

def test_remaining_elements_count_two_elements_sum_even():
    assert remaining_elements_count([2, 6]) == 0

def test_remaining_elements_count_two_elements_sum_odd():
    assert remaining_elements_count([3, 5]) == 0

def test_remaining_elements_count_multiple_elements():  # update
    assert remaining_elements_count([1, 2, 3, 4]) == 4  # update

def test_remaining_elements_count_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_alternating_elements():  # update
    assert remaining_elements_count([1, 2, 3, 2, 1]) == 3  # update

def test_remaining_elements_count_large_even_elements():
    assert remaining_elements_count([2] * 1000) == 0

def test_remaining_elements_count_large_odd_elements():  # update
    assert remaining_elements_count([1] * 1000) == 0  # update
