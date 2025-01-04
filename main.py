from pyray import *
from src.Data import Data
from src.utils import *
from math import ceil

def render(data: Data) -> None:
	grid_player_pos: Vector2 = Vector2(data.player.pos.x/data.tile_size, data.player.pos.y/data.tile_size)
	
	tile_count_x = ceil((get_screen_width() / data.tile_size) / data.cam.zoom)
	tile_count_y = ceil((get_screen_height() / data.tile_size) / data.cam.zoom)

	# Trouver le "start" et le "end" en X/Y
	start_x = int(grid_player_pos.x - tile_count_x / 2 - 1)
	end_x = int(grid_player_pos.x + tile_count_x / 2 + 1)

	start_y = int(grid_player_pos.y - tile_count_y / 2 - 1)
	end_y = int(grid_player_pos.y + tile_count_y / 2 + 1)

	for row_index in range(start_x, end_x):
		for col_index in range(start_y, end_y):
			grid_x = row_index % data.grid_size
			grid_y = col_index % data.grid_size
			screen_x = row_index * data.tile_size
			screen_y = col_index * data.tile_size
			block = data.grid[grid_x][grid_y]
			draw_texture_ex(block.current_image, Vector2(screen_x, screen_y), 0, 1, WHITE)
			if (grid_x == data.mouse_pos.x and grid_y == data.mouse_pos.y):
				draw_texture_ex(data.sprites["selector"][0], Vector2(screen_x, screen_y), 0, 1, WHITE)
	draw_texture_ex(data.player.current_image, (data.player.pos.x - 16, data.player.pos.y - 16), 0, 1, WHITE)


def update_camera(data: Data):
	current_width = get_screen_width()
	current_height = get_screen_height()

	scale_x = current_width / data.SCREEN_WIDTH
	scale_y = current_height / data.SCREEN_HEIGHT
	scale = min(scale_x, scale_y)

	data.cam.zoom = scale + data.ZOOM
	data.cam.offset = Vector2(current_width / 2, current_height / 2)
	data.cam.target = data.player.pos


def draw(data: Data) -> None:
	begin_mode_2d(data.cam)
	clear_background(GRAY)
	render(data)
	end_mode_2d()


def dev(data: Data) -> None:
	draw_rectangle(5, 5, 200, 440, Color(0, 0, 0, 100))
	draw_fps(10, 20)
	t: Block = data.grid[int(data.mouse_pos.x)][int(data.mouse_pos.y)]
	p: Player = data.player
	draw_text(f"{t}\n{p}", 10, 60, 20, WHITE)


def draw_gui(data: Data) -> None:
	dev(data)


def step(data: Data) -> None:
	# Player
	if (data.player.pos.x < 0):
		data.player.pos.x = data.grid_size * data.tile_size
	if (data.player.pos.x > data.grid_size * data.tile_size):
		data.player.pos.x = 0
	if (data.player.pos.y < 0):
		data.player.pos.y = data.grid_size * data.tile_size
	if (data.player.pos.y > data.grid_size * data.tile_size):
		data.player.pos.y = 0

	# Mouse
	mouse_screen_pos = get_mouse_position()
	mouse_world_pos = get_screen_to_world_2d(mouse_screen_pos, data.cam)
	data.mouse_pos.x = int(mouse_world_pos.x // data.tile_size) % data.grid_size
	data.mouse_pos.y = int(mouse_world_pos.y // data.tile_size) % data.grid_size
	if data.mouse_pos.x < 0:
		data.mouse_pos.x = data.grid_size + data.mouse_pos.x
	if data.mouse_pos.y < 0:
		data.mouse_pos.y = data.grid_size + data.mouse_pos.y
	if(is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)):
		block: Block = data.grid[int(data.mouse_pos.x)][int(data.mouse_pos.y)]
		if (block.name != "water"):
			data.grid[int(data.mouse_pos.x)][int(data.mouse_pos.y)] = Block("water", block.pos, data.sprites["water"], 2)
			auto_tiling_area(block, data.grid_size, data.grid, 3)
	zoom_speed = 0.1
	if data.ZOOM < 0.1:
		data.ZOOM= 0.1
	elif data.ZOOM > 5.0:
		data.ZOOM= 5.0

	if is_key_down(KeyboardKey.KEY_P) and data.ZOOM + zoom_speed <= 5.0:
		data.ZOOM += zoom_speed

	if is_key_down(KeyboardKey.KEY_O) and data.ZOOM - zoom_speed >= 0.1:
		data.ZOOM -= zoom_speed


	# Objects
	for obj in data.objects.values():
		obj.update()
		obj.step()
	update_camera(data)


def loop(data: Data) -> None:
	FRAME_DURATION = 1.0 / data.FPS
	time_accumulator = 0.0
	while not window_should_close():
		delat_time = get_frame_time()
		time_accumulator += delat_time

		while time_accumulator >= FRAME_DURATION:
			step(data)
			time_accumulator -= FRAME_DURATION

		begin_drawing()
		draw(data)
		draw_gui(data)
		end_drawing()
	close_window()


if __name__ == "__main__":
	data: Data = Data()
	loop(data)