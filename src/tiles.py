from pyray import *
from src.Entity import *
from src.Player import *
from src.Block import *
from typing import List

TILE: List[int] = [
	11,  # 0b0000
	12,  # 0b0001
	13,  # 0b0010
	6,   # 0b0011
	14,  # 0b0100
	9,   # 0b0101
	0,   # 0b0110
	3,   # 0b0111
	15,  # 0b1000
	8,   # 0b1001
	10,  # 0b1010
	7,   # 0b1011
	2,   # 0b1100
	5,   # 0b1101
	1,   # 0b1110
	4,   # 0b1111
]

DIRECTIONS = [
	(0, -1),	# Top
	(1, 0),		# Right
	(0, 1),		# Bottom
	(-1, 0),	# Left
]

CORNER = [
	(-1, -1),	# Top left
	(1, -1),	# Top Right
	(-1, 1),	# Bottom left
	(1, 1),		# Bottom Right
]


def auto_tiling(block: Block, grid_size: int, grid: List[List[Block]]) -> None:

	ix = int(block.pos.x)
	iy = int(block.pos.y)

	num: int = 0b0000

	for i, (dx, dy) in enumerate(DIRECTIONS):
		nx = (ix + dx) % grid_size
		ny = (iy + dy) % grid_size
		neighbor_block = grid[nx][ny]
		if neighbor_block.name == block.name:
			num |= (1 << i)
			
	tile_index: int = TILE[num]
	if (tile_index < len(block.sprite)):
		block.tile_index = tile_index
		block.current_image = block.sprite[tile_index]

	num = 0b0000
	if (len(block.sprite) == 20):
		for i, (dx, dy) in enumerate(CORNER):
			nx = (ix + dx) % grid_size
			ny = (iy + dy) % grid_size
			neighbor_block = grid[nx][ny]
			if neighbor_block.name != block.name:
					if (i == 0 and tile_index in (4, 5, 7, 8)):		# Top left
						num |= (1 << (i))
					elif (i == 1 and tile_index in (3, 4, 6, 7)):	# Top right
						num |= (1 << (i))
					elif (i == 2 and tile_index in (1, 2, 4, 5)):	# Bottom left
						num |= (1 << (i))
					elif (i == 3 and tile_index in (0, 1, 3, 4)):	# Bottom right
						num |= (1 << (i))
	block.corner_index = num


def auto_tiling_area(block: Block, grid_size: int, grid: List[List[Block]], area: int) -> None:
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