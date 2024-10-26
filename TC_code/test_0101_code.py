import pytest

def remaining_elements_count(a):
    res = []
    for i in a:
        if len(res) == 0:
            res.append(i)
        else:
            if (res[-1] + i) % 2 == 0:
                res.pop()
            else:
                res.append(i)
    return len(res)

def test_empty_list():
    assert remaining_elements_count([]) == 0

def test_single_element():
    assert remaining_elements_count([1]) == 1

def test_two_even_elements():
    assert remaining_elements_count([2, 4]) == 0

def test_two_odd_elements():
    assert remaining_elements_count([1, 3]) == 0

def test_even_and_odd_elements_non_cancelling():
    assert remaining_elements_count([2, 1]) == 2

def test_even_and_odd_elements_cancelling():
    assert remaining_elements_count([2, 3]) == 2

def test_multiple_elements_cancelling():
    assert remaining_elements_count([1, 2, 3, 4]) == 4

def test_large_sequence_with_cancelling():
    assert remaining_elements_count([1, 2, 1, 2, 1, 2]) == 6

def test_large_sequence_without_cancelling():
    assert remaining_elements_count([1, 1, 1, 1, 1, 1]) == 0

def test_alternating_even_and_odd():
    assert remaining_elements_count([1, 2, 1, 2, 1]) == 5

def test_large_even_sequence():
    assert remaining_elements_count([2] * 1000) == 0

def test_large_odd_sequence():
    assert remaining_elements_count([1] * 1000) == 0