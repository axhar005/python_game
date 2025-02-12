from pyray import *
from src.Entity import *
from src.Player import *
from src.Block import *
from src.tiles import *
from typing import Dict
from typing import List

class Data():
	
	def __init__(self) -> None:
		self.SCREEN_WIDTH: int = 960
		self.SCREEN_HEIGHT: int = 540
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, "PtiCraft")
		self.FPS: int = 60
		self.ZOOM: int = 1
		set_target_fps(60)
		self.cam = Camera2D(Vector2(get_screen_width() / 2 - 16, get_screen_height() / 2 - 16), Vector2(0,0), 0, 1)
		self.tile_size = 32
		self.grid_size = 60
		self.mouse_pos: Vector2 = Vector2(0, 0)
		self.mouse_old_block: Block = None
		self.block_hover: Block = None
		self.selected_block: str = ""
		self.selected_index: int = 0
		self.grid_width_px = self.grid_size * self.tile_size
		self.grid_height_px = self.grid_size * self.tile_size
		self.sprites: Dict[str, List[Texture]] = {}
		self.wheel_move: float = 0
		self.old_wheel_move: float = 0
		file: str = "assets/images"
		self.texture_path = {
			"player":		[f"{file}/player/32/player_down_0.png", f"{file}/player/32/player_down_1.png"],
			"dirt": 		[f"{file}/dirt/32/dirt_0.png"],
			"selector": 	[f"{file}/selector.png"],
			"grass":		[f"{file}/grass/32/grass_{i}.png" for i in range(16)],
			"water":		[f"{file}/water/32/water_{i}.png" for i in range(16)],
			"deep_dirt":	[f"{file}/deep_dirt/32/deep_dirt_{i}.png" for i in range(16)],
			"stone_wall": 	[f"{file}/stone/stone_wall/32/stone_wall_{i}.png" for i in range(20)],
			"hill": 		[f"{file}/hill/32/hill_{i}.png" for i in range(20)]
		}
		self.load_texure()
		self.objects: Dict[str, Entity] = {}
		self.objects["player"] = Player("player", Vector2(0, 0), self.sprites["player"])
		self.player = self.objects["player"]
		self.grid: List[List[Block]] = [
			[
				Block("grass", Vector2(row, col), self.sprites["grass"], 0)
				for col in range(self.grid_size)
			]
			for row in range(self.grid_size)
		]
		self.grid[0][0] = Block("water", Vector2(0, 0), self.sprites["water"], 0)
		auto_tiling_area(self.grid[0][0], self.grid_size, self.grid, self.grid_size)

	def load_texure(self) -> None:
		#Gen the air block texture
		# air_img : Image = gen_image_color(32, 32, BLANK)
		# air_texture : Texture2D = load_texture_from_image(air_img)
		# unload_image(air_img)

		# self.sprites["air"] = [air_texture]
		for key, paths in self.texture_path.items():
			self.sprites[key] = [load_texture(path) for path in paths]

	def __str__(self) -> str:
		return f"{self}"