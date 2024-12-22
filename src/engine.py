from pyray import *
from src.Entity import *
from src.Player import *
from src.Block import *
from typing import Dict
from typing import List

class Engine:
	
	def __init__(self) -> None:
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(768, 448, "PtiCraft")
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), Vector2(0,0), 0, 1)
		self.rows, self.cols = 10, 10
		self.sprites: Dict[str, List[Texture]] = {}
		self.texture_path = {
			"player": ["assets/images/player/32/player_down_0.png"],
			"dirt": [],
			"grass": [f"assets/images/grass/32/grass_{i}.png" for i in range(16)],
			"water": [f"assets/images/water/32/water_{i}.png" for i in range(16)],
			"deep_dirt": [f"assets/images/deep_dirt/32/deep_dirt_{i}.png" for i in range(16)],
			"stone": [f"assets/images/stone/stone_wall/32/stone_wall_{i}.png" for i in range(16)]
		}
		self.load_texure()
		self.objects: Dict[str, Entity] = {}
		self.objects["player"] = Player("player", Vector2(0, 0), self.sprites["player"])
		self.player = self.objects["player"]
		self.grid: List[List[Block]] = [
			[
				Block("stone", Vector2(col, row), self.sprites["stone"], 0)
				for col in range(self.cols)
			]
			for row in range(self.rows)
		]
		self.grid[0][0] = Block("water", Vector2(0, 0), self.sprites["water"], 0)

	def load_texure(self) -> None:
		for key, paths in self.texture_path.items():
			self.sprites[key] = [load_texture(path) for path in paths]

	def render(self) -> None:
		grid_width = len(self.grid)
		grid_height = len(self.grid[0])
		grid_player_pos: Vector2 = Vector2(self.player.pos.x/32, self.player.pos.y/32)
		
		start_x = int(grid_player_pos.x - 14)
		end_x = int(grid_player_pos.x + 14)
		start_y = int(grid_player_pos.y - 9)
		end_y = int(grid_player_pos.y + 9)
		
		for row_index in range(start_x, end_x):
			for col_index in range(start_y, end_y):
				grid_x = row_index % grid_width
				grid_y = col_index % grid_height
				screen_x = row_index * 32
				screen_y = col_index * 32
				block = self.grid[grid_x][grid_y]
				draw_texture_ex(
					block.sprite[block.tile_index],
					Vector2(screen_x, screen_y),
					0, 1, WHITE
				)

		draw_texture_ex(self.player.sprite[0], self.player.pos, 0, 1, WHITE)

	def draw(self) -> None:
		begin_mode_2d(self.cam)
		clear_background(GRAY)
		self.render()
		end_mode_2d()

	def draw_gui(self) -> None:
		draw_fps(20, 20)

	def game_step(self) -> None:
		if (self.player.pos.x < 0):
			self.player.pos.x = self.rows * 32
		if (self.player.pos.x > self.rows * 32):
			self.player.pos.x = 0
		if (self.player.pos.y < 0):
			self.player.pos.y = self.cols * 32
		if (self.player.pos.y > self.cols * 32):
			self.player.pos.y = 0
		for obj in self.objects.values():
			obj.step()
		self.cam.target = self.player.pos
	
	def loop(self) -> None:
		while not window_should_close():
			self.delta_time = get_frame_time()
			self.delta_time = min(self.delta_time, 0.5)  # Limite à 50 ms

			self.game_step()
			begin_drawing()
			self.draw()
			self.draw_gui()
			end_drawing()
			#print(f"X: {int(self.player.pos.x)}, Y: {int(self.player.pos.y)}")

	def __str__(self) -> str:
		return f"{self}"