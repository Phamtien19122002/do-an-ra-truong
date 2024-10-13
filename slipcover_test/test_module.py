import pytest
from module import function_a, function_b

def test_function_a_positive():
    assert function_a(5) == 10

def test_function_a_negative():
    assert function_a(-3) == 3

def test_function_b_even():
    assert function_b(4) is True

def test_function_b_odd():
    assert function_b(3) is False
