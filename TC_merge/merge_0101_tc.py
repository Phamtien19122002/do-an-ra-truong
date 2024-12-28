import pytest
from code_0101 import remaining_elements_count
def test_empty_array():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([1]) == 1

def test_two_odd_numbers():  # #update
    assert remaining_elements_count([1, 3]) == 0

def test_two_even_numbers():  # #update
    assert remaining_elements_count([2, 4]) == 0

def test_even_sum_pair_removal():
    assert remaining_elements_count([1, 1, 2, 2]) == 2

def test_odd_sum_pair_removal():
    assert remaining_elements_count([1, 2, 3, 4]) == 4

def test_multiple_removals():  # #update
    assert remaining_elements_count([1, 2, 1, 2, 3, 3]) == 4

def test_large_array_no_removals():
    assert remaining_elements_count([1] * 100000) == 100000

def test_large_array_with_removals():  # #update
    assert remaining_elements_count([2, 2, 1, 1, 3] * 20000) == 20000

def test_interspacing_elements():
    assert remaining_elements_count([1, 2, 1, 3, 2, 3]) == 6

def test_remaining_elements_count_with_multiple_pairing_odd_sum():
    assert remaining_elements_count([1, 2, 3, 4, 5]) == 5

