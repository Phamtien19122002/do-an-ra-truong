import pytest
from code_0101 import remaining_elements_count

def test_remaining_elements_count_empty_list():
    assert remaining_elements_count([]) == 0

def test_remaining_elements_count_single_element():
    assert remaining_elements_count([1]) == 1
    assert remaining_elements_count([2]) == 1

def test_remaining_elements_count_two_even_numbers():  # #update
    assert remaining_elements_count([2, 4]) == 0

def test_remaining_elements_count_two_odd_numbers():  # #update
    assert remaining_elements_count([1, 3]) == 0

def test_remaining_elements_count_odd_even_pair():
    assert remaining_elements_count([1, 2]) == 2

def test_remaining_elements_count_even_odd_pair():
    assert remaining_elements_count([2, 1]) == 2

def test_remaining_elements_count_even_sum_removes_last():  # #update
    assert remaining_elements_count([1, 2, 3]) == 3

def test_remaining_elements_count_odd_sum_removes_last():  # #update
    assert remaining_elements_count([2, 3, 4]) == 3

def test_remaining_elements_count_complex_case():  # #update
    assert remaining_elements_count([1, 2, 3, 4, 5]) == 5

def test_remaining_elements_count_large_list():  # #update
    assert remaining_elements_count(list(range(1, 101))) == 100
