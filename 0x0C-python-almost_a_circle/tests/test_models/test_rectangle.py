#!/usr/bin/python3
"""This module define tests for rectangle module
"""

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
