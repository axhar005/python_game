from pyray import *

class Engine:
	
	def __init__(self):
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(768, 448, "TinyCraft")
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), Vector2(0,0), 0, 1)
		self.sprites = {}
		self.texture_path = {
			"player": [],
			"dirt": [],
			"grass": [f"assets/images/grass/32/grass_{i}.png" for i in range(16)]
		}
		self.load_texure()

	def load_texure(self):
		for key, paths in self.texture_path.items():
			self.sprites[key] = [load_texture(path) for path in paths]

	def draw(self) -> None:
		begin_mode_2d(self.cam)
		clear_background(GRAY)
		#render()
		end_mode_2d()

	def draw_gui(self) -> None:
		draw_fps(20, 20)

	def game_step(self) -> None:
		pass
	
	def loop(self) -> None:
		while not window_should_close():
			self.game_step()
			begin_drawing()
			self.draw()
			self.draw_gui()
			end_drawing()

	def __str__(self):
		return f"{self}"