import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_two_elements_odd_sum():
    assert remaining_elements_count([1, 2]) == 2

def test_remaining_elements_count_two_elements_even_sum():
    assert remaining_elements_count([1, 3]) == 1

def test_remaining_elements_count_three_elements_all_odd():
    assert remaining_elements_count([1, 3, 5]) == 3

def test_remaining_elements_count_three_elements_mixed():
    assert remaining_elements_count([3, 1, 2]) == 2

def test_remaining_elements_count_four_elements_even_out():
    assert remaining_elements_count([2, 4, 6, 8]) == 4

def test_remaining_elements_count_four_elements_combinations():
    assert remaining_elements_count([5, 3, 2, 1]) == 2

def test_remaining_elements_count_large_input():
    assert remaining_elements_count([1] * 1000) == 1

def test_remaining_elements_count_odd_even_pattern():
    assert remaining_elements_count([1, 2, 1, 2]) == 2