from pyray import *
from src.tiles import *
from src.Entity import *
from src.Player import *
from src.Block import *
from src.blocks.Air import Air
from src.blocks.Grass import Grass
from src.blocks.Dirt import Dirt
from src.blocks.Deep_dirt import Deep_dirt
from src.blocks.Sand import Sand
from src.blocks.Water import Water
from src.blocks.Hill import Hill
from src.blocks.Wood_wall import Wood_wall
from src.blocks.Wood_floor import Wood_floor
from src.blocks.Stone_floor import Stone_floor
from src.blocks.Stone_wall import Stone_wall
from typing import Dict
from typing import List

class Data():

	def __init__(self) -> None:
		self.SCREEN_WIDTH: int = 960
		self.SCREEN_HEIGHT: int = 540
		set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
		init_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, "PtiCraft")
		self.FPS: int = 60
		self.zoom: int = 1
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
			"under_player":	[f"{file}/under_player.png"],
			"dirt": 		[f"{file}/dirt/32/dirt_0.png"],
			"selector": 	[f"{file}/selector.png"],
			"grass":		[f"{file}/grass/32/grass_{i}.png" for i in range(16)],
			"water":		[f"{file}/water/32/water_{i}.png" for i in range(16)],
			"sand":			[f"{file}/sand/32/sand_{i}.png" for i in range(16)],
			"deep_dirt":	[f"{file}/deep_dirt/32/deep_dirt_{i}.png" for i in range(16)],
			"wood_floor":	[f"{file}/wood/wood_floor/32/wood_floor.png"],
			"wood_wall": 	[f"{file}/wood/wood_wall/32/wood_wall_{i}.png" for i in range(20)],
			"stone_floor":	[f"{file}/stone/stone_floor/32/stone_floor.png"],
			"stone_wall": 	[f"{file}/stone/stone_wall/32/stone_wall_{i}.png" for i in range(20)],
			"hill": 		[f"{file}/hill/32/hill_{i}.png" for i in range(20)]
		}
		self.load_texure()
		self.objects: Dict[str, Entity] = {}
		self.objects["player"] = Player("player", Vector2(0, 0), self.sprites["player"])
		self.player = self.objects["player"]
		self.block_classes = {
			"air": Air,
			"grass": Grass,
			"dirt": Dirt,
			"deep_dirt": Deep_dirt,
			"water": Water,
			"sand": Sand,
			"wood_wall": Wood_wall,
			"wood_floor": Wood_floor,
			"stone_wall": Stone_wall,
			"stone_floor": Stone_floor,
			"hill": Hill,
		}
		self.block_names = list(self.block_classes.keys())
		
		self.grid: List[List[Block]] = [
			[
				Block("grass", Vector2(row, col), self.sprites["grass"])
				for col in range(self.grid_size)
			]
			for row in range(self.grid_size)
		]
		self.grid[0][0] = Block("water", Vector2(0, 0), self.sprites["water"])
		auto_tiling_area(self.grid[0][0], self.grid_size, self.grid, self.grid_size)

	def set_block(self, pos: Vector2, block_name: str) -> None:
		block_class = self.block_classes.get(block_name)
		if block_class:
			new_block = block_class(pos)
			self.grid[int(pos.x)][int(pos.y)] = new_block
			auto_tiling_area(self.grid[int(pos.x)][int(pos.y)], self.grid_size, self.grid, 3)
		else:
			print(f"Classe de bloc inconnue : {block_name}")


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