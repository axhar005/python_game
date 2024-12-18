from pyray import *
from typing import NamedTuple
from dataclasses import dataclass

class Engine:
	
	def __init__(self):
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(768, 448, "Hello")
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), player.pos, 0, 1)

	def init_texture(self, func) -> None:
		pass

	def draw(self) -> None:
		begin_mode_2d(cam)
		clear_background(GRAY)
		draw_text("Hello world", 190, 200, 20, VIOLET)
		control()
		render()
		end_mode_2d()

	def draw_gui(self) -> None:
		draw_fps(20, 20)

	def loop(self) -> None:
		while not window_should_close():
			begin_drawing()
			self.draw()
			self.draw_gui()
			end_drawing()

	def __str__(self):
		return f"{self}"

@dataclass
class Block:
	name: str
	pos: Vector2
	tiles: int
	layer: int

@dataclass
class Player:
	pos: Vector2


player: Player = Player(Vector2(100, 100))
#rows, cols = 24, 14
rows, cols = 50, 50
grid = [[Block("Air", Vector2(0, 0), 0, 0) for _ in range(cols)] for _ in range(rows)]

image: Image = Image()

tex: Texture = Texture()
ptex: Texture = Texture()

cam: Camera2D = Camera2D()

# Draw grid
#for row in grid:
#	print(row)

def init_texture() -> None:
	global image, tex, cam, player, ptex
	image = load_image("assets/images/dirt_0.png")
	ptex = load_texture("assets/images/player/32/player_down_0.png")
	tex = load_texture_from_image(image)
	cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), player.pos, 0, 1)

def render() -> None:
	global tex, player, ptex
	grid_player_pos: Vector2 = Vector2(player.pos.x/32, player.pos.y/32)
	for row_index, r in enumerate(grid):
		for col_index, c in enumerate(r):
			if ((row_index >= grid_player_pos.x - 13 and row_index <= grid_player_pos.x + 13) and (col_index >= grid_player_pos.y - 8 and col_index <= grid_player_pos.y + 8)):
				draw_texture_ex(tex, Vector2(row_index * 32, col_index * 32), 0, 1, WHITE)
	draw_texture_ex(ptex, player.pos, 0, 1, WHITE)

def control() -> None:
	global player, cam
	cam.target = player.pos
	if (is_key_down(KeyboardKey.KEY_W)):
		player.pos.y -= 0.5
	if (is_key_down(KeyboardKey.KEY_S)):
		player.pos.y += 0.5
	if (is_key_down(KeyboardKey.KEY_A)):
		player.pos.x -= 0.5
	if (is_key_down(KeyboardKey.KEY_D)):
		player.pos.x += 0.5



if __name__ == "__main__":
	engine: Engine = Engine()
	init_texture()
	loop()
	close_window()