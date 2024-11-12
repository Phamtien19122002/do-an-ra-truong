import pytest
from function.function_0101 import remaining_elements_count
def test_remaining_elements_count_with_single_element():
    assert remaining_elements_count([1]) == 1

def test_remaining_elements_count_with_two_odd_elements():
    assert remaining_elements_count([1, 3]) == 2

def test_remaining_elements_count_with_two_even_elements():
    assert remaining_elements_count([2, 4]) == 0

def test_remaining_elements_count_with_one_even_one_odd():
    assert remaining_elements_count([1, 2]) == 2

def test_remaining_elements_count_with_multiple_elements_no_removal():
    assert remaining_elements_count([1, 3, 5, 7]) == 4

def test_remaining_elements_count_with_pairs_removal():
    assert remaining_elements_count([2, 4, 1, 3, 5]) == 3

def test_remaining_elements_count_with_mixed_elements():
    assert remaining_elements_count([1, 2, 3, 4]) == 2

def test_remaining_elements_count_with_maximum_input():
    assert remaining_elements_count(list(range(1, 100001))) == 100000

def test_remaining_elements_count_with_repetitions():
    assert remaining_elements_count([1, 2, 1, 2, 1, 2]) == 6

def test_remaining_elements_count_with_consecutive_pairs():
    assert remaining_elements_count([2, 4, 1, 6, 3]) == 3

def test_remaining_elements_count_with_empty_list():
    assert remaining_elements_count([]) == 0

