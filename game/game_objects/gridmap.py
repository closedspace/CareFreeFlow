from typing import List
from game.game_objects import Line

class GridMap:
    def __init__(self, width: int, height: int, grid_size: int, lines: List[Line]):
        self.width = width
        self.height = height
        self.lines = lines
       