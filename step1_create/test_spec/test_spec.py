import pytest

def reduce_array(A):
    stack = []
    for num in A:
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop()
        else:
            stack.append(num)
    return len(stack)

def test_reduce_array_single_element():
    assert reduce_array([5]) == 1

def test_reduce_array_two_elements_odd_sum():
    assert reduce_array([3, 5]) == 0

def test_reduce_array_two_elements_even_sum():
    assert reduce_array([2, 4]) == 0

def test_reduce_array_three_elements_no_removal():
    assert reduce_array([1, 2, 3]) == 3

def test_reduce_array_four_elements_removal_occur():
    assert reduce_array([2, 1, 3, 4]) == 0

def test_reduce_array_mixed_elements():
    assert reduce_array([5, 1, 2, 6, 3]) == 1

def test_reduce_array_large_input():
    assert reduce_array([1] * 100000) == 0

def test_reduce_array_large_input_boundary():
    assert reduce_array([100] * 100000) == 0

def test_reduce_array_edge_case_empty():
    assert reduce_array([]) == 0

def test_reduce_array_edge_case_one_type():
    assert reduce_array([1] * 100000) == 0