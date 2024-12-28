import pytest
from code_0105 import find_largest_number_from_string

def test_largest_number_in_single_digit():
    result = find_largest_number_from_string("a3b2c1")
    assert result == 3
