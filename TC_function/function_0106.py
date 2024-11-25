import pytest
from function.function_0106 import convert_to_base

def test_convert_to_base_with_valid_binary_string():
    assert convert_to_base('1101', 2) == 'D'

def test_convert_to_base_with_zero_padding():
    assert convert_to_base('01', 2) == '1'

def test_convert_to_base_with_empty_string():
    assert convert_to_base('', 2) == ''

def test_convert_to_base_with_single_digit_binary():
    assert convert_to_base('1', 2) == '1'

def test_convert_to_base_with_non_binary_characters():
    with pytest.raises(ValueError):
        convert_to_base('102', 2)

def test_convert_to_base_with_large_binary_string():
    assert convert_to_base('11111111', 2) == 'FF'

def test_convert_to_base_with_base_two():
    assert convert_to_base('100', 2) == '4'

def test_convert_to_base_with_boundary_length_string():
    assert convert_to_base('0000', 2) == '0'

def test_convert_to_base_with_minimum_length_string():
    assert convert_to_base('0', 2) == '0'

def test_convert_to_base_with_maximum_single_digit_value():
    assert convert_to_base('1111', 2) == 'F'