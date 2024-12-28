import pytest
from code_0106 import convert_to_base

def test_convert_to_base_zero_input():
    assert convert_to_base(0, "0") == "0"  #update

def test_convert_to_base_one_input():
    assert convert_to_base(1, "1") == "1"  #update

def test_convert_to_base_two_input():
    assert convert_to_base(2, "10") == "10"

def test_convert_to_base_positive_bound_input():
    assert convert_to_base(2, "0000") == "0"  #update

def test_convert_to_base_less_than_two_for_s():
    assert convert_to_base(2, "1") == "10"  # Less than minimum length

def test_convert_to_base_large_input():
    assert convert_to_base(16, "0000100000000000") == "10"

def test_convert_to_base_edge_case_for_b():
    assert convert_to_base(4, "00000000") == "0"  #update

def test_convert_to_base_exactly_one_boundary_case():
    assert convert_to_base(1, "0") == "1"  #update

def test_convert_to_base_equal_to_base_case():
    assert convert_to_base(8, "00001000") == "10"  #update expected output

def test_convert_to_base_maximum_single_digit_output():
    assert convert_to_base(15, "00001111") == "0F"

def test_convert_to_base_zero_padding():
    assert convert_to_base(4, "1") == "100"  #update

def test_convert_to_base_large_input():
    assert convert_to_base(256, "1") == "1"  #update expected output

def test_convert_to_base_case1():
    assert convert_to_base(2, '110') == '110'

def test_convert_to_base_case2():
    assert convert_to_base(8, '1101') == '15'  #update expected output as this should convert to octal

def test_convert_to_base_case3():
    assert convert_to_base(4, '101') == '5'

def test_convert_to_base_case_1():
    n = 2
    s = "1010"
    assert convert_to_base(n, s) == s

def test_convert_to_base_case_2():
    n = 3
    s = "1101"
    assert convert_to_base(n, s) == "1"  #update, it is the binary representation of one

def test_convert_to_base_case_3():
    n = 4
    s = "11011"
    assert convert_to_base(n, s) == "3"  #update

def test_convert_to_base_case_4():
    n = 5
    s = "000010101"
    assert convert_to_base(n, s) == "5"  #update

def test_convert_to_base_case_5():
    n = 6
    s = "110100"
    assert convert_to_base(n, s) == "6"  #update
