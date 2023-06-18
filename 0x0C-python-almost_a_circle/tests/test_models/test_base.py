#!/usr/bin/python3
"""This module define test for the Base class
"""

import io
import unittest.mock as mock
from unittest import TestCase
from models.base import Base


class BaseTest(TestCase):
    """Test suite for Base class
    """
    @classmethod
    def setUpClass(cls):
        cls.base_first_no_arg = Base()
        cls.base_id_20 = Base(20)
        cls.base_second_no_arg = Base()
        cls.base_change_id = Base()

    def test_no_args(self):
        """Test Base without argument
        """

        self.assertEqual(self.base_first_no_arg.id, 1)
        self.assertEqual(self.base_second_no_arg.id, 2)

    def test_int_arg(self):
        """Tests Base with integer argument
        """

        self.assertEqual(self.base_id_20.id, 20)

    def test_raise_error(self):
        """Test raise exception when accessing private attribute
        """

        with self.assertRaises(AttributeError):
            self.base_first_no_arg.__nb_objects

    def test_id_change(self):
        """Test that public instance attribute 'id' can be changed
        """

        self.assertEqual(self.base_change_id.id, 3)
        self.base_change_id.id = 7
        self.assertEqual(self.base_change_id.id, 7)

    def test_id_as_string(self):
        """Test id can be set as string value
        """

        base_id_str = Base("id")
        self.assertEqual(base_id_str.id, "id")

    def test_to_json_string_static_method(self):
        list_dict = [{'id': 40, 'x': 5}]

        json_str = Base.to_json_string(list_dict)

        self.assertEqual(type(json_str), str)

        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(json_str)
            self.assertEqual(
                mock_stdout.getvalue(),
                '[{"id": 40, "x": 5}]\n'
                )

    def test_from_json_string(self):
        json_str = '[{"x": 2, "y": 7, "size": 9}]'
        list_of_dict = Base.from_json_string(json_str)

        self.assertEqual(type(list_of_dict), list)
        self.assertEqual(list_of_dict[0]["x"], 2)
        self.assertEqual(
                Base.from_json_string(None),
                []
                )
        self.assertEqual(
                Base.from_json_string([]),
                []
                )
