import arcade

GRID_ROWS = 5
GRID_COLUMNS = 5
GRID_SIZE = 100
CIRCLE_RADIUS = 25

class Game:
    points = []
    def draw_grid(self):
        arcade.draw_lrtb_rectangle_filled(0, GRID_COLUMNS * GRID_SIZE, GRID_ROWS * GRID_SIZE, 0, arcade.color.BLACK)
        for row in range(GRID_ROWS):
            for column in range(GRID_COLUMNS):
                x = column * GRID_SIZE + GRID_SIZE / 2
                y = row * GRID_SIZE + GRID_SIZE / 2
                arcade.draw_rectangle_outline(x, y, GRID_SIZE, GRID_SIZE, arcade.color.SPRING_GREEN)

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x // GRID_SIZE)
        row = int(y // GRID_SIZE)
        x = column * GRID_SIZE + GRID_SIZE / 2
        y = row * GRID_SIZE + GRID_SIZE / 2
        self.points.append((x, y))

    def draw(self):
        arcade.start_render()
        self.draw_grid()
        for point in self.points:
            arcade.draw_circle_filled(point[0], point[1], CIRCLE_RADIUS, arcade.color.CRIMSON_GLORY)


