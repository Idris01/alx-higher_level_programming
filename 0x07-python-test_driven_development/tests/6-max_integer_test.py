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
