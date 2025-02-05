from pyray import *
from typing import List

class Block:
	def __init__(self, name: str, position: Vector2, sprite: List[Texture], tile_index: int) -> None:
		self.name: str = name
		self.pos: Vector2 = position
		self.sprite: List[Texture] = sprite
		self.current_image: Texture = sprite[0]
		self.tile_index: int = 0
		self.corner_index: int = 0b0000

		if (tile_index < len(sprite)):
			self.tile_index = tile_index


	def __str__(self) -> str:
		return f"Name: {self.name:5}\nPos: {int(self.pos.x)},{int(self.pos.y)}\ntile_index: {self.tile_index}\ncorner_index: {self.corner_index}"