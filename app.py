import arcade

grid_size = 50
grid_rows = 10
grid_columns = 10

def on_draw(delta_time):
    arcade.start_render()
    for row in range(grid_rows):
        for column in range(grid_columns):
            x = column * grid_size
            y = row * grid_size
            arcade.draw_rectangle_filled(x + grid_size / 2, y + grid_size / 2, grid_size, grid_size, arcade.color.WHITE)

def on_mouse_press(x, y, button, modifiers):
    column = x // grid_size
    row = y // grid_size
    x = column * grid_size + grid_size / 2
    y = row * grid_size + grid_size / 2
    arcade.draw_circle_filled(x, y, grid_size / 4, arcade.color.RED)

arcade.open_window(grid_columns * grid_size, grid_rows * grid_size, "2D Grid Example")
arcade.set_background_color(arcade.color.BLACK)
arcade.schedule(on_draw, 1 / 60)

window = arcade.get_window()
window.on_mouse_press = on_mouse_press

arcade.run()

