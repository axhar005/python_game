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
	4    # 0b1111
]

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def auto_tiling(block: Block, grid_size: int, grid: List[List[Block]]) -> None:

	ix = int(block.pos.x)
	iy = int(block.pos.y)

	num = 0

	for i, (dx, dy) in enumerate(DIRECTIONS):
		nx = (ix + dx) % grid_size
		ny = (iy + dy) % grid_size

		neighbor_block = grid[nx][ny]
		if neighbor_block.name == block.name:
			num |= (1 << i)


	tile_index: int = TILE[num]
	if (tile_index < len(block.sprite)):
		block.tile_index = TILE[num]
		block.current_image = block.sprite[block.tile_index]


def auto_tiling_area(block: Block, grid_size: int, grid: List[List[Block]], area: int) -> None:
	#block: Block = grid[int(pos.x)][int(pos.y)]
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