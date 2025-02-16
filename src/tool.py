from pyray import *
from src.tiles import *
from src.Data import *
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

class cmd():
	def __init__(self, data: Data):
		self.data = data
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

	def set_block(self, pos: Vector2, block_name: str) -> None:
		block_class = self.block_classes.get(block_name)
		if block_class:
			new_block = block_class(pos, self.data.sprites.get(block_name))
			self.data.grid[int(pos.x)][int(pos.y)] = new_block
			auto_tiling_area(self.data.grid[int(pos.x)][int(pos.y)], self.data.grid_size, self.data.grid, 3)
		else:
			print(f"Classe de bloc inconnue : {block_name}")