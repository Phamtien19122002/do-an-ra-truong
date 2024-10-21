import unittest
from functions.ICPC0105 import find_largest_number_from_string

class TestFindLargestNumberFromString(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(find_largest_number_from_string("12ab29cd19"), 29)
        self.assertEqual(find_largest_number_from_string("ab123gh456cd"), 456)
        self.assertEqual(find_largest_number_from_string("z99y88x77"), 99)
        self.assertEqual(find_largest_number_from_string("hello5world9"), 9)
        self.assertEqual(find_largest_number_from_string("a1b2c3"), 3)

    def test_no_numbers(self):
        self.assertEqual(find_largest_number_from_string("no_digits_here"), float('0'))

    def test_leading_zeros(self):
        self.assertEqual(find_largest_number_from_string("0009abcd010"), 10)

    def test_large_numbers(self):
        self.assertEqual(find_largest_number_from_string("10000000000000000a10000000000000001"), 10000000000000001)

    def test_numbers_within_text(self):
        self.assertEqual(find_largest_number_from_string("qwerty0987654321"), 987654321)
        self.assertEqual(find_largest_number_from_string("onlyone999"), 999)
