import pytest
from code_0104 import find_min_number

def test_multiple_numbers_with_letters():
    assert find_min_number("abc123def456") == 123

