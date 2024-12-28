import pytest
from code_0106 import convert_to_base

def test_convert_to_base_binary_to_base_2():
    result = convert_to_base(2, "0")
    assert result == "0"

def test_convert_to_base_boundary_case_min_length():
    result = convert_to_base(4, "1")
    assert result == "1"

def test_convert_to_base_binary_to_base_16():
    result = convert_to_base(16, "1010")
    assert result == "A"

