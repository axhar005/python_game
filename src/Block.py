from pyray import *
from typing import List

class Block:
	def __init__(self, name: str, position: Vector2, sprite: List[Texture], tile_index: int) -> None:
		self.name: str = name
		self.pos: Vector2 = position
		self.sprite: List[Texture] = sprite
		self.tile_index: int = tile_index

	def __str__(self) -> str:
		return f"{self}"