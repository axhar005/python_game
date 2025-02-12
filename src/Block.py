from pyray import *
from typing import List

class Block:
	def __init__(self, name: str, position: Vector2, sprite: List[Texture], tile_index: int) -> None:
		self.name: str = name
		self.pos: Vector2 = position
		self.sprite: List[Texture] = sprite
		self.current_image: Texture = None
		self.tile_index: int = 0
		self.corner_index: int = 0b0000
		self.sprite_len = 0

		if (sprite):
			self.sprite_len = len(sprite)
			self.current_image = sprite[0]

		if (tile_index < self.sprite_len):
			self.tile_index = tile_index


	def change_sprite(self, sprite: List[Texture]):
		self.sprite = sprite
		self.current_frame = 0
		if (sprite):
			self.sprite_len = len(sprite)
			self.current_image = sprite[0]
		else:
			self.sprite_len = 0
			self.current_image = None


	def update(self) -> None:
		pass


	def step(self) -> None:
		pass


	def __str__(self) -> str:
		return f"Name: {self.name:5}\nPos: {int(self.pos.x)},{int(self.pos.y)}\ntile_index: {self.tile_index}\ncorner_index: {self.corner_index}"