import pytest
from function.function_0101 import remaining_elements_count
def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_odd_elements():
    assert remaining_elements_count([3, 5]) == 2

def test_remaining_elements_count_two_even_elements():
    assert remaining_elements_count([2, 4]) == 2

def test_remaining_elements_count_odd_even_pair():
    assert remaining_elements_count([3, 2]) == 2

def test_remaining_elements_count_four_elements_remain():
    assert remaining_elements_count([1, 2, 3, 4]) == 2

def test_remaining_elements_count_multiple_pairs_removed():
    assert remaining_elements_count([1, 3, 2, 4, 6]) == 1

def test_remaining_elements_count_all_even():
    assert remaining_elements_count([2, 4, 6, 8]) == 4

def test_remaining_elements_count_all_odd():
    assert remaining_elements_count([1, 3, 5, 7]) == 4

def test_remaining_elements_count_large_input_with_pairs():
    assert remaining_elements_count([1] * 100000) == 100000

def test_remaining_elements_count_empty_list():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([1]) == 1
    assert remaining_elements_count([2]) == 1

def test_two_elements_sum_odd():
    assert remaining_elements_count([1, 2]) == 1
    assert remaining_elements_count([2, 4]) == 1

def test_boundary_large_values():
    assert remaining_elements_count([1000000, 1000001, 1000002]) == 2
    assert remaining_elements_count([999999, 1000000]) == 1

def test_boundary_negative_values():
    assert remaining_elements_count([-1, -2, -3]) == 2
    assert remaining_elements_count([-4, -3, -2]) == 1

