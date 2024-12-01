import pytest
from function.function_0101 import remaining_elements_count

def test_empty_list():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([1]) == 1
    assert remaining_elements_count([2]) == 1

def test_two_elements_sum_even():
    assert remaining_elements_count([1, 3]) == 2

def test_two_elements_sum_odd():
    assert remaining_elements_count([1, 2]) == 1
    assert remaining_elements_count([2, 4]) == 1

def test_multiple_elements_even_odd():
    assert remaining_elements_count([1, 2, 3, 4]) == 2

def test_multiple_elements_odd_even():
    assert remaining_elements_count([3, 5, 7, 2]) == 4

def test_alternating_even_odd():
    assert remaining_elements_count([2, 1, 4, 3]) == 1

def test_boundary_large_values():
    assert remaining_elements_count([1000000, 1000001, 1000002]) == 2
    assert remaining_elements_count([999999, 1000000]) == 1

def test_boundary_negative_values():
    assert remaining_elements_count([-1, -2, -3]) == 2
    assert remaining_elements_count([-4, -3, -2]) == 1