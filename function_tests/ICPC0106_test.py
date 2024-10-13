import unittest
from functions.ICPC0106 import convert_to_base

class TestConvertToBase(unittest.TestCase):

    def test_base_2(self):
        self.assertEqual(convert_to_base("1101", 2), "1101")
        self.assertEqual(convert_to_base("1010", 2), "1010")

    def test_base_4(self):
        self.assertEqual(convert_to_base("1101", 4), "31")
        self.assertEqual(convert_to_base("1010", 4), "22")

    def test_base_8(self):
        self.assertEqual(convert_to_base("1101", 8), "15")
        self.assertEqual(convert_to_base("1010", 8), "12")

    def test_base_16(self):
        self.assertEqual(convert_to_base("1101", 16), "D")
        self.assertEqual(convert_to_base("1010", 16), "A")

    def test_padding(self):
        self.assertEqual(convert_to_base("1", 4), "1")
        self.assertEqual(convert_to_base("11", 8), "3")
        self.assertEqual(convert_to_base("111", 16), "7")

    def test_large_number(self):
        self.assertEqual(convert_to_base("111100001111", 16), "F0F")
        self.assertEqual(convert_to_base("111111111111", 16), "FFF")
