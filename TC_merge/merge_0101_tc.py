import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_odds():  #update
    assert remaining_elements_count([1, 3]) == 2  # Odds don't remove each other

def test_remaining_elements_count_one_odd_one_even():
    assert remaining_elements_count([1, 2]) == 2  # An odd and an even don't remove each other

