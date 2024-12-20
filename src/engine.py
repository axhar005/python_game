from pyray import *
from src.Entity import *
from src.Player import *
from typing import Dict

class Engine:
	
	def __init__(self):
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(768, 448, "PtiCraft")
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), Vector2(0,0), 0, 1)
		self.rows, self.cols = 50, 50
		self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
		self.sprites: Dict[str, Texture] = {}
		self.texture_path = {
			"player": [],
			"dirt": [],
			"grass": [f"assets/images/grass/32/grass_{i}.png" for i in range(16)],
			"water": [f"assets/images/water/32/water_{i}.png" for i in range(16)]
		}
		self.load_texure()
		self.objects: Dict[str, Entity] = {}
		self.objects["player"] = Player("player", Vector2(0, 0), self.sprites["grass"][4])

	def load_texure(self):
		for key, paths in self.texture_path.items():
			self.sprites[key] = [load_texture(path) for path in paths]

	def render(self):
		grid_player_pos: Vector2 = Vector2(self.objects["player"].pos.x/32, self.objects["player"].pos.y/32)
		for row_index, r in enumerate(self.grid):
			for col_index, c in enumerate(r):
				if ((row_index >= grid_player_pos.x - 13 and row_index <= grid_player_pos.x + 13) and (col_index >= grid_player_pos.y - 8 and col_index <= grid_player_pos.y + 8)):
					draw_texture_ex(self.sprites["water"][0], Vector2(row_index * 32, col_index * 32), 0, 1, WHITE)
		draw_texture_ex(self.objects["player"].texture, self.objects["player"].pos, 0, 1, WHITE)

	def draw(self) -> None:
		begin_mode_2d(self.cam)
		clear_background(GRAY)
		self.render()
		end_mode_2d()

	def draw_gui(self) -> None:
		draw_fps(20, 20)

	def game_step(self) -> None:
		for obj in self.objects.values():
			obj.step()
		self.cam.target = self.objects["player"].pos
	
	def loop(self) -> None:
		while not window_should_close():
			self.delta_time = get_frame_time()
			self.delta_time = min(self.delta_time, 0.5)  # Limite à 50 ms

			self.game_step()
			begin_drawing()
			self.draw()
			self.draw_gui()
			end_drawing()

	def __str__(self):
		return f"{self}"