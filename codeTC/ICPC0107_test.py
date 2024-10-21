import unittest
from functions.ICPC0107 import process_cases

class TestProcessCases(unittest.TestCase):

    def test_basic_case_1(self):
        cases = [
            (("1", "2"), ("123", "456")),
        ]
        expected = [
            (569, 679),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_basic_case_2(self):
        cases = [
            (("3", "4"), ("345", "678")),
        ]
        expected = [
            (1013, 1123),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_basic_case_3(self):
        cases = [(("5", "6"), ("567", "890")),]
        expected = [(1447, 1557),]
        self.assertEqual(process_cases(1, cases), expected)

    def test_single_digit_replacement_1(self):
        cases = [
            (("1", "9"), ("123", "456")),
        ]
        expected = [
            (579, 1379),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_single_digit_replacement_2(self):
        cases = [
            (("2", "8"), ("234", "567")),
        ]
        expected = [
            (801, 1401),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_no_replacement_1(self):
        cases = [
            (("1", "1"), ("123", "456")),
        ]
        expected = [
            (579, 579),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_no_replacement_2(self):
        cases = [
            (("2", "2"), ("234", "567")),
        ]
        expected = [
            (801, 801),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_edge_case_1(self):
        cases = [
            (("0", "9"), ("000", "000")),
        ]
        expected = [
            (0, 1998),
        ]
        self.assertEqual(process_cases(1, cases), expected)

    def test_edge_case_2(self):
        cases = [
            (("9", "0"), ("999", "999")),
        ]
        expected = [
            (0, 1998),
        ]
        self.assertEqual(process_cases(1, cases), expected)
