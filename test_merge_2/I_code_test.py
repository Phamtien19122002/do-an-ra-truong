import pytest
from I_code import remaining_elements_count

def test_remaining_elements_count_empty():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([1]) == 1

def test_remaining_elements_count_two_elements_even_sum():
    assert remaining_elements_count([1, 3]) == 0  

def test_remaining_elements_count_two_elements_odd_sum():
    assert remaining_elements_count([1, 2]) == 2 

def test_remaining_elements_count_multiple_elements():
    assert remaining_elements_count([1, 2, 3, 4]) == 4

def test_remaining_elements_count_multiple_elements_with_pops():
    assert remaining_elements_count([1, 1, 2, 2]) == 0

def test_remaining_elements_count_with_negative_numbers():
    assert remaining_elements_count([-1, 1]) == 0

def test_remaining_elements_count_with_zeros():
    assert remaining_elements_count([0, 0]) == 0

def test_remaining_elements_count_with_large_numbers():
    assert remaining_elements_count([10**9, 10**9]) == 0

def test_remaining_elements_count_mixed():
    assert remaining_elements_count([1, 2, 3, 4, 5, 6]) == 6

def test_remaining_elements_count_complex():
    assert remaining_elements_count([1, 1, 2, 3, 3, 2, 4, 4]) == 0

def test_remaining_elements_count_alternating_even_odd():
    assert remaining_elements_count([1, 2, 1, 2, 1, 2]) == 6

def test_remaining_elements_count_all_even_numbers():
    assert remaining_elements_count([2, 4, 6, 8]) == 0

def test_remaining_elements_count_all_odd_numbers():
    assert remaining_elements_count([1, 3, 5, 7]) == 0

def test_remaining_elements_count_large_input():
    assert remaining_elements_count([1, 2] * 1000) == 2000