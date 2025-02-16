import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_odds():  #update
    assert remaining_elements_count([1, 3]) == 2  # Odds don't remove each other

def test_remaining_elements_count_two_evens():  #update
    assert remaining_elements_count([2, 4]) == 2  # Evens don't remove each other

def test_remaining_elements_count_one_odd_one_even():
    assert remaining_elements_count([1, 2]) == 2  # An odd and an even don't remove each other

def test_remaining_elements_count_multiple_elements_no_removal():
    assert remaining_elements_count([1, 3, 5, 7]) == 4  # All odds, no removal

def test_remaining_elements_count_multiple_removals():  #update
    assert remaining_elements_count([2, 4, 1, 3, 6]) == 1  # Pairs will be removed

def test_remaining_elements_count_boundaries():
    assert remaining_elements_count([100]) == 1
    assert remaining_elements_count([1, 100]) == 2

def test_remaining_elements_count_large_list_with_removals():  #update
    assert remaining_elements_count([1] * 99999 + [2]) == 2  # All odds plus an even, remove them all

def test_remaining_elements_count_large_list_no_removals():  #update
    assert remaining_elements_count([1] * 100000) == 100000  # All odds, no removal
