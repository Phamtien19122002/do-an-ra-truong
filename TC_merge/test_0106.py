import pytest
import math

def test_convert_to_base_valid_case_2():
    assert convert_to_base(2, "1010") == 10

def test_convert_to_base_valid_case_4():
    assert convert_to_base(4, "210") == 2 * 4**2 + 1 * 4**1 + 0 * 4**0 == 32 + 4 + 0 == 36

def test_convert_to_base_valid_case_8():
    assert convert_to_base(8, "100010") == 2 * 8**1 + 0 * 8**0 == 64 + 0 == 64

def test_convert_to_base_valid_case_16():
    assert convert_to_base(16, "A3") == 10 * 16**1 + 3 * 16**0 == 160 + 3 == 163

def test_convert_to_base_invalid_base_case():
    with pytest.raises(ValueError):
        convert_to_base(3, "1010")

def test_convert_to_base_invalid_binary_case():
    with pytest.raises(ValueError):
        convert_to_base(2, "10201")

def test_convert_to_base_boundary_case_min_length():
    assert convert_to_base(2, "0") == 0
    assert convert_to_base(2, "1") == 1

def test_convert_to_base_boundary_case_max_length():
    binary_str = "1" * 100000
    assert convert_to_base(2, binary_str) == 2**100000 - 1

def test_convert_to_base_valid_input():
    assert convert_to_base("1100", 2) == "12"

