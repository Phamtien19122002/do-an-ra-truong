import pytest
from code_0101 import remaining_elements_count

def test_empty_list():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([1]) == 1

def test_two_elements_even_sum():
    assert remaining_elements_count([2, 2]) == 0

def test_two_elements_odd_sum():
    assert remaining_elements_count([1, 2]) == 2

def test_multiple_elements_even_sum_cancel():
    assert remaining_elements_count([1, 1, 2, 2]) == 0

def test_multiple_elements_odd_sum_remain():
    assert remaining_elements_count([1, 2, 3]) == 3

def test_consecutive_elements_cancel():
    assert remaining_elements_count([1, 3, 2, 4]) == 2

def test_boundary_even_and_odd():
    assert remaining_elements_count([0, 1, 2]) == 3

def test_large_numbers():
    assert remaining_elements_count([1000000000, 1000000001]) == 2