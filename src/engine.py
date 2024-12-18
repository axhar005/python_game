from pyray import *


def load_texture(path):
	sprites = {}
	for key, paths in path.items():
		sprites[key] = [load_texture(path) for path in paths]  # Charge chaque texture pour chaque clé
	return sprites

class Engine:
	
	def __init__(self):
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(768, 448, "Hello")
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), Vector2(0,0), 0, 1)
		self.sprites = {
			"player": [],
			"dirt": [],
			"grass": ["assets\images\grass\32\grass_0.png"]
		}

	def draw(self) -> None:
		begin_mode_2d(self.cam)
		clear_background(GRAY)
		draw_text("Hello world", 190, 200, 20, VIOLET)
		#render()
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