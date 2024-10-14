import pytest
from src import remaining_elements_count

def test_single_element():
    A = [1]
    assert remaining_elements_count(A) == 1

def test_two_elements_even_sum():
    A = [2, 4]
    assert remaining_elements_count(A) == 0

def test_two_elements_odd_sum():
    A = [1, 2]
    assert remaining_elements_count(A) == 2

def test_three_elements_no_removal():
    A = [1, 3, 5]
    assert remaining_elements_count(A) == 3

def test_three_elements_with_removal():
    A = [2, 4, 3]
    assert remaining_elements_count(A) == 1

def test_four_elements_overlapping_removals():
    A = [2, 4, 6, 1]
    assert remaining_elements_count(A) == 2

def test_all_even_sum_pairs_even_length():
    A = [2, 4, 6, 8]
    assert remaining_elements_count(A) == 0

def test_all_even_sum_pairs_odd_length():
    A = [2, 4, 6, 8, 10]
    assert remaining_elements_count(A) == 1

def test_no_removals():
    A = [1, 3, 5, 7]
    assert remaining_elements_count(A) == 0

def test_alternating_even_odd():
    A = [1, 2, 3, 4, 5]
    assert remaining_elements_count(A) == 5

def test_large_input_no_removals():
    A = [1] * 100000
    assert remaining_elements_count(A) == 0

def test_large_input_with_one_remaining():
    A = [1] * 100001
    assert remaining_elements_count(A) == 1

def test_mixed_removals():
    A = [1, 2, 2, 1, 3, 4, 4, 3]
    assert remaining_elements_count(A) == 0

def test_alternating_removals():
    A = [2, 1, 2, 1, 2, 1]
    assert remaining_elements_count(A) == 0

def test_no_elements():
    A = []
    assert remaining_elements_count(A) == 0