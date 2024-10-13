import pytest
from src import remaining_elements_count

def test_empty_input():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([1]) == 1

def test_pop_condition():
    assert remaining_elements_count([1, 1]) == 0

def test_append_condition():
    assert remaining_elements_count([1, 2]) == 2

def test_multiple_operations_pop_and_append():
    assert remaining_elements_count([1, 3, 2, 4]) == 0

def test_complex_case():
    assert remaining_elements_count([1, 2, 3, 4, 5]) == 3

def test_all_pops():
    assert remaining_elements_count([2, 2, 2, 2]) == 0

def test_alternating_append_pop():
    assert remaining_elements_count([1, 2, 1, 2, 1, 2]) == 0

def test_no_pops():
    assert remaining_elements_count([1, 3, 5, 7]) == 4

def test_mixed_operations():
    assert remaining_elements_count([1, 2, 3, 5, 4, 6, 7]) == 3
