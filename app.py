import arcade
from game.game_objects import Game

GRID_ROWS = 5
GRID_COLUMNS = 5
GRID_SIZE = 100

class GridWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.game = Game()

    def on_draw(self):
        self.game.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        self.game.on_mouse_press(x, y, button, modifiers)

if __name__ == '__main__':
    window = GridWindow(GRID_COLUMNS * GRID_SIZE, GRID_ROWS * GRID_SIZE)
    arcade.run()
