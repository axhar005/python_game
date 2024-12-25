from pyray import *
from src.Entity import *
from src.Player import *
from src.Block import *
from typing import Dict
from typing import List

def auto_tiling(pos: Vector2, grid_size: int, grid: List[List[Block]]) -> None:
	
	block: Block = grid[int(pos.x)][int(pos.y)]
	position: Vector2 = block.pos
	num = 0
	
	def wrap(value: int, max_value: int) -> int:
		if value < 0:
			return max_value - 1
		elif value >= max_value:
			return 0
		return value

	neighbors: Dict[str, Block] = {
		"top": grid[int(position.x)][wrap(int(position.y) - 1, grid_size)],
		"bottom": grid[int(position.x)][wrap(int(position.y) + 1, grid_size)],
		"left": grid[wrap(int(position.x) - 1, grid_size)][int(position.y)],
		"right": grid[wrap(int(position.x) + 1, grid_size)][int(position.y)],
	}
	
	direction_indices = {"top": 0, "right": 1, "bottom": 2, "left": 3}

	for direction, neighbor in neighbors.items():
		i = direction_indices[direction]
		if (block.name == neighbor.name):
			num |= 1 << i

	tile: Dict[bin, int] = {
		0b0110: 0,
		0b1110: 1,
		0b1100: 2,
		0b0111: 3,
		0b1111: 4,
		0b1101: 5,
		0b0011: 6,
		0b1011: 7,
		0b1001: 8,
		0b0101: 9,
		0b1010: 10,
		0b0000: 11,
		0b0001: 12,
		0b0010: 13,
		0b0100: 14,
		0b1000: 15
	}
	block.tile_index = tile[num]
	'''
	print("\n")
	for key, value in neighbors.items():
		print(str(f"{key:6} -> {value}"))
	print(str(f"{block}"))
	'''
	
def auto_tiling_area(pos: Vector2, grid_size: int, grid: List[List[Block]], area: int) -> None:
	block: Block = grid[int(pos.x)][int(pos.y)]
	center_x = int(block.pos.x)
	center_y = int(block.pos.y)
	offset = area // 2
	
	for dy in range(-offset, offset + 1):
		for dx in range(-offset, offset + 1):
			x = center_x + dx
			y = center_y + dy
			
			x %= grid_size
			y %= grid_size
			
			neighbor_block = grid[x][y]
			auto_tiling(neighbor_block, grid_size, grid)