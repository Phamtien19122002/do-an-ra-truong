import pytest
from functions.ICPC0101 import remaining_elements_count

def test_remaining_elements_count_empty():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([1]) == 1

def test_remaining_elements_count_no_removal():
    assert remaining_elements_count([1, 3, 5]) == 1

def test_remaining_elements_count_all_removed():
    assert remaining_elements_count([1, 1, 2, 2]) == 0

def test_remaining_elements_count_some_removed():
    assert remaining_elements_count([1, 2, 3, 4, 5]) == 5

def test_remaining_elements_count_alternating():
    assert remaining_elements_count([1, 2, 3, 4, 5, 6]) == 6

def test_remaining_elements_count_complex():
    assert remaining_elements_count([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9

def test_remaining_elements_count_large_input():
    large_input = [i for i in range(1000000)]
    assert remaining_elements_count(large_input) == 1000000

def test_remaining_elements_count_all_even():
    assert remaining_elements_count([2, 4, 6, 8]) == 0

def test_remaining_elements_count_all_odd():
    assert remaining_elements_count([1, 3, 5, 7]) == 0

def test_remaining_elements_count_mixed():
    assert remaining_elements_count([1, 2, 3, 2, 1]) == 5

def test_remaining_elements_count_zero():
    assert remaining_elements_count([0, 0, 0, 0]) == 0

def test_remaining_elements_count_zero_and_odd():
    assert remaining_elements_count([0, 1, 0, 1]) == 4

def test_remaining_elements_count_zero_and_even():
    assert remaining_elements_count([0, 2, 0, 2]) == 0
