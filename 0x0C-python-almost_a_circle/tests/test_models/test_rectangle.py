#!/usr/bin/python3
"""This module define tests for rectangle module
"""
import io
import unittest.mock as mock
from unittest import TestCase
from models.rectangle import Rectangle


class RectangleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        width = 10
        height = 6
        cls.width = width
        cls.height = height
        x, y = (5, 3)
        cls.x = x
        cls.y = y
        cls.rectangle_from_origin = Rectangle(width, height)
        cls.rectangle_with_coord = Rectangle(width, height, x, y)

    def test_rect_measurements(self):
        """Test rectangle  width and height are corretly set
        """

        rect = self.rectangle_from_origin
        self.assertEqual(rect.width, self.width)
        self.assertEqual(rect.height, self.height)
        self.assertTrue(rect.x == 0)
        self.assertTrue(rect.y == 0)

    def test_rect_axis(self):
        """Test axis of rectangle correctly set
        """

        rect = self.rectangle_with_coord
        self.assertEqual(rect.x, self.x)
        self.assertEqual(rect.y, self.y)

    def test_rect_private_attribute_not_accessible(self):
        """Test private attributes are not accessible
        """

        rect = self.rectangle_from_origin
        with self.assertRaises(AttributeError):
            rect.__x
        with self.assertRaises(AttributeError):
            rect.__y
        with self.assertRaises(AttributeError):
            rect.__width
        with self.assertRaises(AttributeError):
            rect.__height

    def test_rectangle_id(self):
        """Test rectangle id correctly set
        """
        rect_1 = self.rectangle_from_origin
        rect_2 = self.rectangle_with_coord

        self.assertEqual(rect_1.id, 1)
        self.assertEqual(rect_2.id, 2)

    def test_rectangle_with_incomplete_parameters(self):
        """Test that rectangle requires width and height
        """
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_rectangle_attributes_updated(self):
        """Test that rectangle width, height, x, y and id can be updated
        """

        rect = Rectangle(width=7, height=5, id=200)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.id, 200)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        rect.width = 20
        rect.height = 13
        rect.id = 220
        rect.x, rect.y = (3, 4)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 13)
        self.assertEqual(rect.id, 220)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_width_must_be_integer(self):
        """Test that rectangle raises exception if width is not integer
        """

        with self.assertRaises(TypeError) as error:
            Rectangle("5", 3)
        self.assertEqual('width must be an integer', str(error.exception))

        rect = Rectangle(5, 3)
        with self.assertRaises(TypeError) as error_2:
            rect.width = "5"
        self.assertEqual('width must be an integer', str(error_2.exception))

    def test_height_must_be_integer(self):
        """Test that rectangle raises exception if height is not integer
        """

        with self.assertRaises(TypeError) as error:
            Rectangle(5, "3")
        self.assertEqual('height must be an integer', str(error.exception))

        rect = Rectangle(5, 3)
        with self.assertRaises(TypeError) as error_2:
            rect.height = "5"
        self.assertEqual('height must be an integer', str(error_2.exception))

    def test_width_is_greater_than_zero(self):
        """Test that rectangle raises exception if width <= 0
        """

        with self.assertRaises(ValueError) as error:
            Rectangle(-1, 3)
        self.assertEqual('width must be > 0', str(error.exception))

        rect = Rectangle(5, 3)
        with self.assertRaises(ValueError) as error_2:
            rect.width = 0
        self.assertEqual('width must be > 0', str(error_2.exception))

    def test_height_is_greater_than_zero(self):
        """Test that rectangle raises exception if height <= 0
        """

        with self.assertRaises(ValueError) as error:
            Rectangle(6, -2)
        self.assertEqual('height must be > 0', str(error.exception))

        rect = Rectangle(5, 3)
        with self.assertRaises(ValueError) as error_2:
            rect.height = 0
        self.assertEqual('height must be > 0', str(error_2.exception))

    def test_x_and_y_is_integer(self):
        """Test that setting x or y as non integer raises Exception
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(5, 2, "4", 4)
        self.assertEqual('x must be an integer', str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(5, 2, 4, "4")
        self.assertEqual('y must be an integer', str(error.exception))

        rect = Rectangle(5, 2)
        with self.assertRaises(TypeError) as error:
            rect.y = "4"
        self.assertEqual('y must be an integer', str(error.exception))

        with self.assertRaises(TypeError) as error:
            rect.x = 0.5
        self.assertEqual('x must be an integer', str(error.exception))

    def test_x_and_y_greater_or_equal_zero(self):
        """Test that exception raised for value of x or y below 0
        """

        with self.assertRaises(ValueError) as error:
            Rectangle(5, 2, -1, 4)
        self.assertEqual('x must be >= 0', str(error.exception))
        with self.assertRaises(ValueError) as error:
            Rectangle(5, 2, 4, -1)
        self.assertEqual('y must be >= 0', str(error.exception))

        rect = Rectangle(5, 2)
        with self.assertRaises(ValueError) as error:
            rect.y = -10
        self.assertEqual('y must be >= 0', str(error.exception))

        with self.assertRaises(ValueError) as error:
            rect.x = -9
        self.assertEqual('x must be >= 0', str(error.exception))

    def test_area_5_by_6_is_30(self):
        """Test that area of a rectangle returns expected result
        """

        rect = Rectangle(5, 6)
        self.assertEqual(rect.area(), 30)

    def test_area_with_parameter_raises_exception(self):
        """Test that area does'nt require any argument
        """

        rect = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            rect.area(3)

    def test_rectangle_display(self):
        """Test that the rectangle is printed out with # symbol
        """

        rect1 = Rectangle(2, 3, 0, 0)
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect1.display()
            self.assertEqual(mock_stdout.getvalue(), '##\n##\n##\n')

    def test_rectangle_display_with_coordinate(self):
        """Test that the rectangle is printed out with # symbol
        """

        rect1 = Rectangle(2, 3, 3, 2)
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect1.display()
            self.assertEqual(
                    mock_stdout.getvalue(),
                    '\n\n   ##\n   ##\n   ##\n'
                    )

    def test_call_display_with_arg_raise_exception(self):
        """Test that rectangle display method should receive no argument
        """

        rect = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            rect.display(4)

    def test_rectangle_string_representation(self):
        """Test rectangle string representation
        """
        rect = Rectangle(4, 7, 4, 5, 12)
        self.assertEqual(str(rect), '[Rectangle] (12) 4/5 - 4/7')
