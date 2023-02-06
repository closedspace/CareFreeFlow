import arcade
from typing import List, Tuple
from game.game_objects import Point
class Line:
    """A line object
    :param color: The color of the line
    :param start_point: The start point of the line
    :param end_point: The end point of the line
    :param list_of_points: The list of points that make up the line

    :type color: arcade.color
    :type start_point: Point
    :type end_point: Point
    :type list_of_points: list[Point]
    
    :Example:
    >>> line = Line(arcade.color.RED, Point(arcade.color.RED, 0, 0), Point(arcade.color.RED, 100, 100), [Point(arcade.color.RED, 0, 0), Point(arcade.color.RED, 100, 100)])
    >>> line.draw()
    >>> line.get_start_point()
    Point(arcade.color.RED, 0, 0)
    >>> line.get_end_point()
    Point(arcade.color.RED, 100, 100)
    >>> line.get_list_of_points()
    [Point(arcade.color.RED, 0, 0), Point(arcade.color.RED, 100, 100)]
    >>> line.get_color()
    arcade.color.RED
    >>> line.set_start_point(Point(arcade.color.RED, 50, 50))
    >>> line.set_end_point(Point(arcade.color.RED, 150, 150))
    >>> line.set_list_of_points([Point(arcade.color.RED, 50, 50), Point(arcade.color.RED, 150, 150)])
    >>> line.set_color(arcade.color.BLUE)
    """
    def __init__(self, color: Tuple[float, float, float, float], start_point: int, end_point: int, list_of_points: List[Point]):
        self.color = color
        self.start_point = start_point
        self.end_point = end_point
        self.list_of_points = list_of_points
    def get_start_point(self):
        return self.start_point
    def get_end_point(self):
        return self.end_point
    def get_list_of_points(self):
        return self.list_of_points
    def get_color(self):
        return self.color
    def set_start_point(self, start_point):
        self.start_point = start_point
    def set_end_point(self, end_point):
        self.end_point = end_point
    def set_list_of_points(self, list_of_points):
        self.list_of_points = list_of_points
    def set_color(self, color):
        self.color = color
