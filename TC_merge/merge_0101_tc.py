import pytest
from code_0101 import remaining_elements_count
def test_single_element():
    assert remaining_elements_count([7]) == 1

def test_two_odds():
    assert remaining_elements_count([3, 5]) == 2  #update

def test_odd_even_pair():
    assert remaining_elements_count([1, 2]) == 2

