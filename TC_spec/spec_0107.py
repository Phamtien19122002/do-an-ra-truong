import pytest
from function.function_0107 import process_cases

def test_minimum_sum_with_same_digits():
    assert process_cases("1 1 123 321") == "444"

def test_maximum_sum_with_same_digits():
    assert process_cases("2 2 456 654") == "1110"

def test_minimum_sum_with_different_digits():
    assert process_cases("1 2 1122 2211") == "4444"

def test_maximum_sum_with_different_digits():
    assert process_cases("0 9 0000 9999") == "9999"

def test_large_number_case_minimum_sum():
    assert process_cases("3 7 300000000000000000000 700000000000000000000") == "1000000000000000000000"

def test_large_number_case_maximum_sum():
    assert process_cases("5 6 999999999999999999999 555555555555555555555") == "1555555555555555555554"

def test_case_with_zero_boundary():
    assert process_cases("0 1 0 1") == "1"

def test_case_with_max_boundary():
    assert process_cases("5 6 " + "5" * 1000 + " " + "6" * 1000) == str(int("5" * 1000) + int("6" * 1000))