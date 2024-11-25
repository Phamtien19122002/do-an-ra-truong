import pytest
from function.function_0106 import convert_to_base

def test_binary_to_base_2():
    assert convert_to_base(2, "10010100010010101") == "224225"

def test_binary_to_base_4():
    assert convert_to_base(4, "10010100010010101") == "331135"

def test_binary_to_base_8():
    assert convert_to_base(8, "10010100010010101") == "224225"

def test_binary_to_base_16():
    assert convert_to_base(16, "10010100010010101") == "00000000DC84"

def test_binary_input_length_minimum():
    assert convert_to_base(2, "0") == "0"
    assert convert_to_base(2, "1") == "1"

def test_binary_input_length_maximum():
    binary_string = '1' * 100000
    assert convert_to_base(2, binary_string) == '1' * 100000

def test_invalid_base_raises_error():
    with pytest.raises(ValueError):
        convert_to_base(3, "10010100010010101")

def test_non_binary_string_raises_error():
    with pytest.raises(ValueError):
        convert_to_base(2, "100202")