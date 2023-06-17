#!/usr/bin/python3
"""This module define unittest for Square
"""


from unittest import TestCase
from models.square import Square


class SquareTest(TestCase):
    """Test suit for Square class
    """

    def test_size_is_height_and_width(self):
        square = Square(4)
        self.assertEqual(square.size, square.height)
        self.assertEqual(square.width, square.height)

    def tests_square_string_representation(self):
        square = Square(5, 7, 9, id=10)
        sqr_str = '[Square] (10) 7/9 - 5'
        self.assertEqual(str(square), sqr_str)

    def test_square_size_setter_getter(self):
        square = Square(5, 7, 9, id=10)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_square_size_with_wrong_value(self):
        square = Square(5, 7, 9, id=10)

        with self.assertRaises(TypeError) as err:
            square.size = "5"
        self.assertEqual(
                str(err.exception),
                "width must be an integer"
                )

        with self.assertRaises(ValueError) as err:
            square.size = -5
        self.assertEqual(
                str(err.exception),
                "width must be > 0"
                )
