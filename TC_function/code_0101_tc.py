import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_with_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_with_single_element():
    assert remaining_elements_count([1]) == 1

def test_remaining_elements_count_with_two_elements_sum_even():
    assert remaining_elements_count([2, 2]) == 0

def test_remaining_elements_count_with_two_elements_sum_odd():
    assert remaining_elements_count([1, 2]) == 2

def test_remaining_elements_count_with_three_elements_same_parity():  # update
    assert remaining_elements_count([1, 3, 5]) == 3  # update

def test_remaining_elements_count_with_three_elements_different_parity():  # update
    assert remaining_elements_count([1, 2, 3]) == 3  # update

def test_remaining_elements_count_with_large_even_pair():  # update
    assert remaining_elements_count([4, 6, 8, 10, 12]) == 5  # update

def test_remaining_elements_count_with_large_odd_pair():  # update
    assert remaining_elements_count([5, 7, 9, 11]) == 4  # update

def test_remaining_elements_count_with_mixed_series():
    assert remaining_elements_count([1, 2, 1, 2, 3, 4]) == 6  # update

def test_remaining_elements_count_with_no_removals():
    assert remaining_elements_count([1, 4, 3, 2]) == 4
