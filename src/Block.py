from pyray import *
from typing import List

class Block:
	def __init__(self, name: str, position: Vector2, sprite: List[Texture], tile_index: int) -> None:
		self.name: str = name
		self.pos: Vector2 = position
		self.sprite: List[Texture] = sprite
		self.current_sprite: Texture = sprite[0]
		if (tile_index < len(sprite)):
			self.tile_index = tile_index
		else:
			self.tile_index = 0

	def __str__(self) -> str:
		return f"Name: {self.name:5} | Pos: {int(self.pos.x)},{int(self.pos.y)} | tile_index: {self.tile_index}"