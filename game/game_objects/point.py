from typing import Tuple
import arcade

class Point:
    """
    A point object
    :param color: The color of the point
    :param x: The x coordinate of the point
    :param y: The y coordinate of the point
    
    :type color: Tuple[float, float, float, float]
    :type x: int
    :type y: int
    
    :Example:
    >>> point = Point((255, 0, 0, 255), 0, 0)
    >>> point.get_color()
    (255, 0, 0, 255)
    >>> point.get_x()
    0
    >>> point.get_y()
    0
    >>> point.set_color((0, 0, 255, 255))
    >>> point.set_x(100)
    >>> point.set_y(100)
    """
    def __init__(self, color: Tuple[float, float, float, float], x: int, y: int, radius: int = 25):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
    def get_color(self) -> Tuple[float, float, float, float]:
        return self.color
    def get_x(self) -> int:
        return self.x
    def get_y(self) -> int:
        return self.y
    def set_color(self, color: Tuple[float, float, float, float]):
        self.color = color
    def set_x(self, x: int):
        self.x = x
    def set_y(self, y: int):
        self.y = y
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

