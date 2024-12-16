import pytest
from code_0101 import remaining_elements_count
def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_odd_elements():  # update
    assert remaining_elements_count([3, 5]) == 0

def test_remaining_elements_count_two_even_elements():  # update
    assert remaining_elements_count([2, 4]) == 0

def test_remaining_elements_count_odd_even_pair():
    assert remaining_elements_count([1, 2]) == 2

def test_remaining_elements_count_multiple_pairs():
    assert remaining_elements_count([1, 3, 2, 4]) == 0

def test_remaining_elements_count_with_large_numbers():
    assert remaining_elements_count([99, 13, 2, 8, 7]) == 1

def test_remaining_elements_count_all_pairs_removable():
    assert remaining_elements_count([2, 2, 4, 4]) == 0

def test_remaining_elements_count_large_array():  # update
    assert remaining_elements_count([1] * 100000) == 0

def test_remaining_elements_count_mixed_pairs():
    assert remaining_elements_count([1, 6, 3, 2, 5]) == 5

def test_remaining_elements_count_with_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_with_odd_length_even_sum():  # update
    assert remaining_elements_count([1, 2, 3]) == 3

def test_remaining_elements_count_with_large_even_length():
    assert remaining_elements_count([1, 2] * 500) == 0

def test_remaining_elements_count_with_large_odd_length():  # update
    assert remaining_elements_count([1, 2, 3] * 333 + [4]) == 4

