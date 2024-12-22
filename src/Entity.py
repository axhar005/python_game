from pyray import *
from typing import List

class Entity:
	def __init__(self, name: str, position: Vector2, sprite: List[Texture]) -> None:
		self.name: str = name
		self.pos: Vector2 = position
		self.sprite: List[Texture] = sprite
		self.velocity: Vector2 = Vector2(0, 0)

	def step(self) -> None:
		pass