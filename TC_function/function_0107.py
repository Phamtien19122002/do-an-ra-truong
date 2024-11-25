import pytest
from function.function_0107 import process_cases

def test_process_cases_replacement_only_one_char():
    assert process_cases('1', '2', '1', '2') == (3, 3)

def test_process_cases_no_replacement():
    assert process_cases('1', '2', '3', '4') == (3, 3)

def test_process_cases_replacement_multiple_chars():
    assert process_cases('121', '212', '1', '2') == (454, 454)

def test_process_cases_replacement_empty_string():
    assert process_cases('', '', '1', '2') == (0, 0)

def test_process_cases_same_replacement():
    assert process_cases('123', '456', '3', '3') == (579, 579)

def test_process_cases_larger_numbers():
    assert process_cases('1000', '2000', '0', '1') == (3001, 3001)

def test_process_cases_boundary_replacement():
    assert process_cases('9999', '9998', '9', '0') == (9998, 9999)

def test_process_cases_multiple_characters():
    assert process_cases('hello', 'hello', 'l', 'w') == (hewlo, hewlo)

def test_process_cases_single_digit_numbers():
    assert process_cases('3', '5', '3', '5') == (8, 8)