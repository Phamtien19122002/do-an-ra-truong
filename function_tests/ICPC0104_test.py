import unittest
from functions.ICPC0104 import find_min_number

class TestFindMinNumber(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(find_min_number("abc123xyz"), 123)
        self.assertEqual(find_min_number("a1b2c3"), 1)
        self.assertEqual(find_min_number("x10y20z30"), 10)

    def test_no_numbers(self):
        self.assertEqual(find_min_number("abcdef"), 10**19)

    def test_numbers_only(self):
        self.assertEqual(find_min_number("123456"), 10**19)

    def test_multiple_numbers(self):
        self.assertEqual(find_min_number("4a2b3c1d5e"), 1)
        self.assertEqual(find_min_number("99x88y77z66"), 77)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(find_min_number("   12ab34cd56"), 12)

    def test_empty_string(self):
        self.assertEqual(find_min_number(""), 10**19)
