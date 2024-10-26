import pytest

def remove_even_sum_pairs(arr):
    stack = []
    for num in arr:
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop()
        else:
            stack.append(num)
    return len(stack)

def test_remove_even_sum_pairs_single_element():
    assert remove_even_sum_pairs([5]) == 1

def test_remove_even_sum_pairs_two_odd_elements():
    assert remove_even_sum_pairs([3, 5]) == 0

def test_remove_even_sum_pairs_two_even_elements():
    assert remove_even_sum_pairs([2, 4]) == 0

def test_remove_even_sum_pairs_mixed_elements():
    assert remove_even_sum_pairs([1, 2, 3, 4, 5]) == 5

def test_remove_even_sum_pairs_multiple_even_and_odd():
    assert remove_even_sum_pairs([1, 3, 2, 4, 5, 7]) == 0

def test_remove_even_sum_pairs_large_input():
    assert remove_even_sum_pairs([1] * 100000) == 0

def test_remove_even_sum_pairs_all_even_large_input():
    assert remove_even_sum_pairs([2] * 100000) == 0

def test_remove_even_sum_pairs_all_odd_large_input():
    assert remove_even_sum_pairs([1] * 100000) == 0

def test_remove_even_sum_pairs_no_pairs():
    assert remove_even_sum_pairs([1, 2, 3, 4]) == 4

def test_remove_even_sum_pairs_alternating_pairs():
    assert remove_even_sum_pairs([1, 2, 1, 2, 1]) == 5