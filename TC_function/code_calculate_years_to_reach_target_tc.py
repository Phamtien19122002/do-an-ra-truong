import pytest
from code_calculate_years_to_reach_target import calculate_years_to_reach_target

def test_calculate_years_to_reach_target_with_negative_initial_amount():
    result = calculate_years_to_reach_target(-1000, 5, 2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_zero_initial_amount():
    result = calculate_years_to_reach_target(0, 5, 2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_none_initial_amount():
    result = calculate_years_to_reach_target(None, 5, 2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_negative_interest_rate():
    result = calculate_years_to_reach_target(1000, -5, 2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_zero_interest_rate():
    result = calculate_years_to_reach_target(1000, 0, 2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_none_interest_rate():
    result = calculate_years_to_reach_target(1000, None, 2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_negative_target():
    result = calculate_years_to_reach_target(1000, 5, -2000)
    assert result == "None"

def test_calculate_years_to_reach_target_with_zero_target():
    result = calculate_years_to_reach_target(1000, 5, 0)
    assert result == "None"

def test_calculate_years_to_reach_target_with_none_target():
    result = calculate_years_to_reach_target(1000, 5, None)
    assert result == "None"

def test_calculate_years_to_reach_target_with_positive_values():
    result = calculate_years_to_reach_target(1000, 5, 2000)
    assert result == 15

def test_calculate_years_to_reach_target_with_high_interest_rate():
    result = calculate_years_to_reach_target(1000, 20, 5000)
    assert result == 6

def test_calculate_years_to_reach_target_with_exact_target():
    result = calculate_years_to_reach_target(1000, 100, 100000)
    assert result == 5