#!/usr/bin/python3
"""This module define the Base class
"""

import os
import json
import turtle


class Base:
  """Base class

    Args:
        id (int): id of the instance

    Attributes:
        __nb_objects (int): number of active instance
        of the class
    """
  __nb_objects = 0

  def __init__(self, id=None):
    """Initializes instance by setting the id
        """

    if id is not None:
      self.id = id
    else:
      Base.__nb_objects += 1
      self.id = Base.__nb_objects

  @staticmethod
  def to_json_string(list_dictionaries):
    """Convert list of dictionary to json format

        Args:
            list_dictionaries (list): list of dict

        Returns:
            json string representation

        """

    list_dict = list_dictionaries

    if list_dict is None or not list_dict:
      return "[]"

    return json.dumps(list_dict)

  @classmethod
  def save_to_file(cls, list_objs):
    """Save objects contain in list_objs to file

        Args:
            list_objs (list): list of objects that are
            derived from Base

        """

    if list_objs is None or not list_objs:
      with open('Base.json', 'w', encoding='utf-8') as stream:
        stream.write("[]")
        return

    name = f"{type(list_objs[0]).__name__}.json"
    list_dict = [obj.to_dictionary() for obj in list_objs]

    with open(name, 'w', encoding="utf-8") as f:
      f.write(cls.to_json_string(list_dict))

  @staticmethod
  def from_json_string(json_string):
    """Convert from json to python list type

        Args:
            json_string (str): json string representation

        Returns:
            list of python dictionary
        """

    if json_string is None or not json_string:
      return []

    return json.loads(json_string)

  @classmethod
  def create(cls, **dictionary):
    """Create a new instance from dictionary

        Args:
            dictionary (dict): attrubutes of new object
        Returns:
            newly created instance of cls

        """

    if cls.__name__ != 'Base':
      new_obj = cls(2, 3)
    else:
      new_obj = cls()

    new_obj.update(**dictionary)

    return new_obj

  @classmethod
  def load_from_file(cls):
    """Load list of instances of class from file

        The file name is of form <classname>.json in the current
        dirrectory

        Returns:
            list of instances

        """
    file_name = f"{cls.__name__}.json"
    if not os.path.exists(file_name):
      return []

    with open(file_name, 'r', encoding="utf-8") as stream:
      dict_list = cls.from_json_string(stream.read())

    return [cls.create(**attr) for attr in dict_list]

  @classmethod
  def save_to_file_csv(cls, list_objs):
    """Save attributes of objects to file in csv format

        Args:
            list_objs (list): list of objects

        """
    name = cls.__name__
    file_name = "{}.csv".format(name)

    if name == 'Square':
      attr_list = ['id', 'size', 'x', 'y']
    elif name == 'Rectangle':
      attr_list = ['id', 'width', 'height', 'x', 'y']

    with open(file_name, 'w', encoding="utf-8") as f:
      size = len(list_objs)

      for index, obj in enumerate(list_objs):
        attr = obj.to_dictionary()
        attr_vals = [str(attr[indx]) for indx in attr_list]
        if index == size - 1:
          f.write(f"{','.join(attr_vals)}")
        else:
          f.write(f"{','.join(attr_vals)}\n")

  @classmethod
  def load_from_file_csv(cls):
    """Load instances of class from file into a list
        """

    file_name = "{}.csv".format(cls.__name__)

    if not os.path.exists(file_name):
      return []

    new_list = []

    with open(file_name, 'r', encoding="utf-8") as f:

      line = f.readline()
      while line != '':
        data = [int(val) for val in line.split(',')]

        if cls.__name__ == 'Base':
          new_obj = cls()  # dummy object of Base class
        else:
          new_obj = cls(1, 2)  # dummy object of other class

        new_obj.update(*data)  # set correct object data
        new_list.append(new_obj)  # add object to list

        line = f.readline()  # read next line in file

    return new_list

  @staticmethod
  def draw(list_rectangles, list_squares):
    """Draw rectangles and square in list_rectangles and list_square
    Args:
      list_rectangles (list): list of rectangle objects
      list_squares (list): list of squares
    """

    def _draw(pen, width, height, color='red'):
      """Draws on the screen

      Args:
        pen: instance of turtle.Turtle
        width (int): width of the shape
        height (int): height of the shape
        color (str): color to use for drawing
      """
      pen.pendown()
      pen.color(color)
      pen.forward(width)
      pen.left(90)
      pen.forward(height)
      pen.left(90)
      pen.forward(width)
      pen.left(90)
      pen.forward(height)
      pen.left(90)
      pen.penup()

    screen = turtle.getscreen()
    pen = turtle.Turtle()

    start_point = -screen.window_width() / 2
    max_height = 0
    pen.penup()
    pen.forward(start_point)
    if list_rectangles:
      next_start = 0
      for rect in list_rectangles:
        attr = rect.to_dictionary()
        width, height = (attr['width'], attr['height'])
        if height > max_height:
          max_height = height
        _draw(pen, width, height)
        next_start += width + (width / 2)
        pen.forward(next_start)

    if list_squares:
      pen.goto(0, 0)
      pen.forward(start_point)
      pen.left(-90)
      pen.forward(max_height * 2)
      pen.left(90)

      next_start = 0
      for sqr in list_squares:
        attr = sqr.to_dictionary()
        width, height = (attr['size'], attr['size'])
        _draw(pen, width, height, color='green')
        next_start += width + width / 2
        pen.forward(next_start)
    screen.exitonclick()