from pyray import *
from src.Engine import *
from typing import NamedTuple
from dataclasses import dataclass

@dataclass
class Block:
	name: str
	pos: Vector2
	tiles: int
	layer: int

@dataclass
class Player:
	pos: Vector2

#rows, cols = 24, 14
rows, cols = 50, 50
grid = [[Block("Air", Vector2(0, 0), 0, 0) for _ in range(cols)] for _ in range(rows)]

# Draw grid
#for row in grid:
#	print(row)
'''
def render() -> None:
	global tex, player, ptex
	grid_player_pos: Vector2 = Vector2(player.pos.x/32, player.pos.y/32)
	for row_index, r in enumerate(grid):
		for col_index, c in enumerate(r):
			if ((row_index >= grid_player_pos.x - 13 and row_index <= grid_player_pos.x + 13) and (col_index >= grid_player_pos.y - 8 and col_index <= grid_player_pos.y + 8)):
				draw_texture_ex(tex, Vector2(row_index * 32, col_index * 32), 0, 1, WHITE)
	draw_texture_ex(ptex, player.pos, 0, 1, WHITE)
'''

if __name__ == "__main__":
	engine: Engine = Engine()
	engine.loop()
	close_window()