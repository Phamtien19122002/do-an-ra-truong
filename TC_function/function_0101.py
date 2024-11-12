import pytest
from function.function_0101 import remaining_elements_count

def test_remaining_elements_count_with_single_element():
    assert remaining_elements_count([5]) == 1

def test_remaining_elements_count_with_two_odd_elements():
    assert remaining_elements_count([3, 5]) == 2

def test_remaining_elements_count_with_two_even_elements():
    assert remaining_elements_count([2, 4]) == 2

def test_remaining_elements_count_with_even_and_odd_elements():
    assert remaining_elements_count([2, 3]) == 1

def test_remaining_elements_count_with_odd_and_even_elements():
    assert remaining_elements_count([5, 2]) == 2

def test_remaining_elements_count_with_multiple_elements_resulting_in_empty():
    assert remaining_elements_count([1, 3, 2, 4]) == 0

def test_remaining_elements_count_with_increasing_elements():
    assert remaining_elements_count([1, 2, 3, 4, 5]) == 3

def test_remaining_elements_count_with_decreasing_elements():
    assert remaining_elements_count([5, 4, 3, 2, 1]) == 3

def test_remaining_elements_count_with_mixed_elements():
    assert remaining_elements_count([1, 3, 2, 1]) == 2

def test_remaining_elements_count_with_identical_elements():
    assert remaining_elements_count([5, 5, 5, 5]) == 4

def test_remaining_elements_count_with_empty_list():
    assert remaining_elements_count([]) == 0