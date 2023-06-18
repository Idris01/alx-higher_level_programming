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

    def test_square_update_args(self):
        sqr = Square(5, 7, 3, 22)
        sqr.update(9)
        self.assertEqual(sqr.id, 9)
        sqr.update(9, 4)
        self.assertEqual(sqr.size, 4)
        sqr.update(9, 4, 10)
        self.assertEqual(sqr.x, 10)
        sqr.update(9, 4, 10, 8)
        self.assertEqual(sqr.y, 8)

    def test_square_update_kwargs(self):
        sqr = Square(11, 3, 2, 13)
        sqr.update(id=20)
        self.assertEqual(sqr.id, 20)
        sqr.update(size=21)
        self.assertEqual(sqr.size, 21)
        sqr.update(x=7, y=18)
        self.assertEqual(sqr.x, 7)
        self.assertEqual(sqr.y, 18)

    def test_square_update_args_over_kwargs(self):
        sqr = Square(11, 3, 2, 13)
        sqr.update(25, id=18)
        self.assertEqual(sqr.id, 25)

    def test_square_to_dict(self):
        sqr = Square(34, 3, 7, id=40)
        sqr_dict = {
                'size': 34, 'x': 3, 'y': 7, 'id': 40
                }

        self.assertEqual(
                sqr_dict,
                sqr.to_dictionary()
                )

        self.assertEqual(
                type(sqr.to_dictionary()),
                dict
                )

        with self.assertRaises(TypeError):
            sqr.to_dictionary(5)

    def test_square_create(self):
        sqr = Square(3, 4, 7, 8)
        sqr_dict = sqr.to_dictionary()
        sqr2 = sqr.create(**sqr_dict)
        sqr2_dict = sqr2.to_dictionary()

        self.assertEqual(sqr_dict, sqr2_dict)
