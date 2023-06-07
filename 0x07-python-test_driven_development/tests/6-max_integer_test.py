#!/usr/bin/python3
"""Unittest for max-integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger (unittest.TestCase):
    """Setup different test cases for max-integer function
    """
    def setUp(self):
        self.int_list = [1, 2, 8, 11, 50]
        self.mixed_data = [5, "9", 'ade', []]
        self.max_start = [20, 11, 8, 17]
        self.max_middle = [1, 2, 100, 3, 7]
        self.negative_list = [-1, -2, -4]
        self.one_negative_list = [-3, 10, 21]

    def test_integer_passed(self):
        self.assertEqual(max_integer(self.int_list), 50)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_raise_exception_for_list_in_list(self):
        with self.assertRaises(Exception):
            max_integer(self.mixed_data)

    def test_raise_exception_for_integer_as_argument(self):
        with self.assertRaises(Exception):
            max_integer(5)

    def test_max_exist_at_middle(self):
        self.assertEqual(max_integer(self.max_middle), 100)

    def test_max_exist_at_start(self):
        self.assertEqual(max_integer(self.max_start), 20)

    def test_max_single_element(self):
        self.assertEqual(max_integer([2]), 2)

    def test_negative_max(self):
        self.assertEqual(max_integer(self.negative_list), -1)

    def test_one_negative_in_list(self):
        self.assertEqual(max_integer(self.one_negative_list), 21)
