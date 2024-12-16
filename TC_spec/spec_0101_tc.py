import pytest
from code_0101 import remaining_elements_count

def test_single_element():
    assert remaining_elements_count([5]) == 1

def test_two_odd_elements(): 
    assert remaining_elements_count([3, 5]) == 2  # update

def test_two_even_elements():
    assert remaining_elements_count([4, 2]) == 0

def test_one_odd_one_even():
    assert remaining_elements_count([8, 5]) == 2

def test_three_elements_one_pair_removal():
    assert remaining_elements_count([1, 2, 3]) == 3  # update

def test_multiple_elements_all_removable():
    assert remaining_elements_count([1, 3, 2, 4, 6]) == 1

def test_multiple_elements_none_removable():
    assert remaining_elements_count([1, 3, 5, 7]) == 4  # update

def test_large_numbers_with_removable_pairs():
    assert remaining_elements_count([100, 99, 2, 4, 101]) == 1

def test_large_numbers_with_no_removable_pairs():
    assert remaining_elements_count([2, 4, 6, 8]) == 0

def test_boundary_condition_max_elements():
    assert remaining_elements_count([1] * (10**5)) == 0
