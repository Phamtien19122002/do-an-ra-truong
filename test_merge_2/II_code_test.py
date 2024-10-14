from II_code import find_min_number

def test_find_min_number_basic():
    assert find_min_number("123a456b789c") == 123

def test_find_min_number_no_numbers():
    assert find_min_number("abcdef") == 10 ** 19

def test_find_min_number_digits_not_followed_by_letters():
    assert find_min_number("123456789") == 10 ** 19

def test_find_min_number_empty_string():
    assert find_min_number("") == 10 ** 19

def test_find_min_number_digits_followed_by_non_alpha():
    assert find_min_number("123!456@") == 10 ** 19

def test_find_min_number_mixed():
    assert find_min_number("12a34!56b78c") == 12

def test_find_min_number_large_numbers():
    assert find_min_number("9999999999999999999a1b") == 1

def test_find_min_number_number_equal_to_res():
    assert find_min_number(str(10 ** 19) + "a") == 10 ** 19

def test_find_min_number_number_exceeding_res():
    assert find_min_number(str(10 ** 19 + 1) + "a") == 10 ** 19

def test_find_min_number_single_digit_followed_by_letter():
    assert find_min_number("7z") == 7

def test_find_min_number_digit_followed_by_digit_and_letter():
    assert find_min_number("56a78") == 56

def test_find_min_number_digit_sequence_not_followed_by_letter():
    assert find_min_number("123456") == 10 ** 19

def test_find_min_number_digit_followed_by_letter_and_digit():
    assert find_min_number("5a5") == 5

def test_find_min_number_non_digit_followed_by_letter():
    assert find_min_number("@a") == 10 ** 19

def test_find_min_number_digit_followed_by_digit_and_non_letter():
    assert find_min_number("123#") == 10 ** 19
