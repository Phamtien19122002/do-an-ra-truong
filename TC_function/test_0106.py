import pytest
import math

def convert_to_base(s, n):
    c = ['A', 'B', 'C', 'D', 'E', 'F']
    b = int(math.log(n, 2))
    if n == 2:
        return s
    while len(s) % b != 0:
        s = "0" + s
    result = ""
    i = 0
    while i < len(s):
        tmp = 0
        for j in range(i, i + b):
            tmp += int(s[j]) * (2 ** (b - j + i - 1))
        if tmp < 10:
            result += str(tmp)
        else:
            result += c[tmp - 10]
        i += b
    
    return result

def test_convert_to_base_valid_input():
    assert convert_to_base("1100", 2) == "12"

def test_convert_to_base_zero():
    assert convert_to_base("0", 2) == "0"

def test_convert_to_base_single_digit():
    assert convert_to_base("1", 2) == "1"

def test_convert_to_base_empty_string():
    assert convert_to_base("", 2) == ""

def test_convert_to_base_boundary_condition():
    assert convert_to_base("11111111", 2) == "FF"

def test_convert_to_base_invalid_length():
    assert convert_to_base("100", 2) == "4"

def test_convert_to_base_all_ones():
    assert convert_to_base("111111111111", 2) == "FF"

def test_convert_to_base_large_input():
    assert convert_to_base("111111111111111111", 2) == "FFFFFF"