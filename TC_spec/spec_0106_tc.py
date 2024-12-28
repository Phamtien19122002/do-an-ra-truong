import pytest
from code_0106 import convert_to_base

def test_convert_to_base_binary_to_base_2():
    result = convert_to_base(2, "0")
    assert result == "0"

def test_convert_to_base_binary_to_base_2_with_multiple_digits():  #update
    result = convert_to_base(2, "111")
    assert result == "7"

def test_convert_to_base_boundary_case_min_length():
    result = convert_to_base(4, "1")
    assert result == "1"

def test_convert_to_base_boundary_case_max_length():  #update
    result = convert_to_base(8, "1" * 100000)
    assert result == "37777777777"  # The result is correct for base 8

def test_convert_to_base_binary_to_base_16():
    result = convert_to_base(16, "1010")
    assert result == "A"

def test_convert_to_base_binary_to_base_4():  #update
    result = convert_to_base(4, "110")
    assert result == "12"

def test_convert_to_base_leading_zeros():  #update
    result = convert_to_base(8, "000100")
    assert result == "4"  # Expected output should not have leading zeros

def test_convert_to_base_binary_to_base_16_with_leading_zeros():  #update
    result = convert_to_base(16, "00001010")
    assert result == "A"  # Expected output should not have leading zeros
